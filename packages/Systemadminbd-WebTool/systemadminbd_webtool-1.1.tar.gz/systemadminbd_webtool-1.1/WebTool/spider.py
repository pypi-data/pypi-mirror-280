import os
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag, urlparse
import hashlib
import requests,urllib
import re,threading
import chardet
from colorama import Fore, Style, init
import fake_useragent
import queue
init(autoreset=True)
requests.urllib3.disable_warnings()
banner="""
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗ █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██████╗ ██████╗ 
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██╔══██╗
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║███████║██║  ██║██╔████╔██║██║██╔██╗ ██║██████╔╝██║  ██║
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██╔══██╗██║  ██║
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██████╔╝██████╔╝
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚═════╝"""
def clear_terminal():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and other Unix-like systems
        os.system('clear')
    os.system(f"echo \"\"\"{banner}\"\"\" | lolcat")
    os.system(f"echo \"\"\"\t\t\t\t\t  Coded By Systemadminbd\"\"\" | lolcat")
    print("\n\n")
# Define colorama colors for logging
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

async def fetch(session, url, semaphore):
    async with semaphore:
        try:
            url = url.replace("http://", "https://")
            headers = {
                'User-Agent': fake_useragent.UserAgent().random
            }

            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    print(f"{fc}Successfully fetched: {url}")
                    try:
                        content = await response.read()
                        detected_encoding = chardet.detect(content)['encoding']
                        if not detected_encoding:
                            return None, None

                        try:
                            text = content.decode(detected_encoding)
                            return text, urllib.parse.unquote(url)
                        except (UnicodeDecodeError, LookupError):
                            encodings = ['utf-8', 'iso-8859-1', 'latin1', 'windows-1252']
                            for encoding in encodings:
                                try:
                                    text = content.decode(encoding)
                                    return text, urllib.parse.unquote(url)
                                except (UnicodeDecodeError, LookupError):
                                    continue
                    except Exception:
                        pass
                else:
                    pass
        except Exception:
            pass
    return None, None

def extract_links(html, base_url):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        for tag in soup.find_all('a', href=True):
            href = tag.get('href')
            href = urljoin(base_url, href)
            href, _ = urldefrag(href)
            if urlparse(href).netloc == urlparse(base_url).netloc:
                links.add(href)
        return links
    except Exception:
        return set()

def extract_files_and_dirs(html, base_url):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        files_and_dirs = set()
        for tag in soup.find_all(['a', 'link', 'script'], href=True):
            href = tag.get('href')
            full_url = urljoin(base_url, href)
            path = urlparse(full_url).path
            files_and_dirs.add(path)
        for tag in soup.find_all('img', src=True):
            src = tag.get('src')
            full_url = urljoin(base_url, src)
            path = urlparse(full_url).path
            if "base64" not in path:
                files_and_dirs.add(path)
        for tag in soup.find_all('script', src=True):
            src = tag.get('src')
            full_url = urljoin(base_url, src)
            path = urlparse(full_url).path
            files_and_dirs.add(path)
        return files_and_dirs
    except Exception:
        return set()

def file_already_exists(local_path, file_content):
    try:
        if os.path.exists(local_path):
            existing_file_hash = hashlib.md5(open(local_path, 'rb').read()).hexdigest()
            new_file_hash = hashlib.md5(file_content).hexdigest()
            return existing_file_hash == new_file_hash
    except Exception:
        pass
    return False

def write_file(url, local_path, file_content):
    try:
        if not os.path.isdir(local_path):
            if not os.path.exists(os.path.dirname(local_path)):
                os.makedirs(os.path.dirname(local_path), exist_ok=True)

            if not file_already_exists(local_path, file_content):
                with open(local_path, 'wb') as f:
                    f.write(file_content)
                print(f"{fg}Downloaded {url} to {Fore.MAGENTA}{local_path}")
            else:
                print(
                    f"{fy}Skipped downloading {url} to {Fore.MAGENTA}{local_path} (already exists with same content)")
        else:
            pass
    except Exception:
        pass

def create_empty_file(local_path):
    try:
        if not os.path.exists(local_path):
            with open(local_path, 'w') as f:
                pass
            print(f"Created empty file: {local_path}")
    except Exception as e:
        print(f"Error creating empty file {local_path}: {e}")

async def create_local_path(base_dir, path):
    try:
        local_path = os.path.join(base_dir, path.lstrip('/'))
        decode_local_path = urllib.parse.unquote(local_path)
        return decode_local_path
    except Exception as e:
        print(f"{fr}An error occurred while creating local path {local_path}: {e}")
        return None

async def download_file(session, url, local_path, semaphore,base_dir, retries=1):
    headers = {
        'User-Agent': fake_useragent.UserAgent().random
    }
    async with semaphore:
        for attempt in range(retries):
            try:
                if os.path.exists(local_path):
                    print(
                        f"{fy}Skipped before downloading {url} to {Fore.MAGENTA}{local_path} (already exists with same content)")
                    return
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        try:
                            file_content = await response.read()
                            if file_content.strip():
                                if url.endswith(('.pdf', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg',  # Images and PDFs
                                                 '.mp3', '.wav', '.aac', '.flac', '.ogg',  # Audio
                                                 '.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm',  # Video
                                                 '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.odt', '.ods', '.odp'  # Documents
                                                 )):
                                    threading.Thread(target=write_file, args=(url, local_path, file_content)).start()
                                else:
                                    loop = asyncio.get_running_loop()
                                    await loop.run_in_executor(None, write_file, url, local_path, file_content)
                                    #save all urll here
                                    with open(base_dir+"/urls.txt","a") as f:
                                    	f.write(url+"\n" )#writing all file names except images,video and audio
                            else:
                                    pass
                        except Exception:
                            pass
                    else:
                        pass
            except Exception as e:
                print(f"{fr}Exception occurred while downloading {url}: {e}")
            await asyncio.sleep(0)

async def crawl(session, url, visited, semaphore, base_dir):
    if url in visited:
        return
    visited.add(url)

    html, fetched_url = await fetch(session, url, semaphore)
    if html:
        links = extract_links(html, url)
        files_and_dirs = extract_files_and_dirs(html, url)

        for item in files_and_dirs:
            local_path = await create_local_path(base_dir, item)
            if local_path:
                await download_file(session, urljoin(fetched_url, item), local_path, semaphore,base_dir)

        for link in links:
            if link not in visited:
                await crawl(session, link, visited, semaphore, base_dir)
    else:
        pass

def get_url(url):
    try:
        excluded_extensions = ('.pdf', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg',  # Images and PDFs
                               '.mp3', '.wav', '.aac', '.flac', '.ogg',  # Audio
                               '.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm',  # Video
                               '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.odt', '.ods', '.odp'  # Documents
                               )

        if url.endswith('/'):
            match = re.search(r'^(?:https?:\/\/)?(?:www\.)?([^\/]+)', url[:-1])
            if match:
                return "https://" + match.group(1)
        elif url.endswith(excluded_extensions):
            match = re.search(r'^(?:https?:\/\/)?(?:www\.)?([^\/]+)', url)
            if match:
                return "https://" + match.group(1)
        else:
            if not url.startswith('http://'):
                url = 'https://' + url.lstrip('https://')
            match = re.match(r'https://(?:www\.)?([^\/]+)', url)
            if match:
               
                return url
            else:
                match2 = re.search(r'^(?:https?:\/\/)?(?:www\.)?([^\/]+)', url)
                if match2:
                    return "https://" + match2.group(1)
    except Exception as e:
        return None

async def worker(session, to_visit, visited, semaphore, processed_paths):
    while not to_visit.empty():
        try:
            url = await asyncio.to_thread(to_visit.get)
            match = re.search(r'^(?:https?:\/\/)?(?:www\.)?([^\/]+)', url)

            if not match or not url:
                print(f"Invalid URL: {url}")
                continue

            domain = match.group(1)
            try:
                url = get_url(url)
            except Exception as e:
                print(f"Error fetching URL {url}: {e}")
                continue

            base_dir = os.path.join(os.getcwd()+"/spider/", domain)

            if not processed_paths:
                initial_paths = ["/index.html", "/index.php"]
                for path in initial_paths:
                    initial_url = urljoin("https://" + domain, path)
                    await crawl(session, initial_url, visited, semaphore, base_dir)
                    processed_paths.add(initial_url)

            await crawl(session, url, visited, semaphore, base_dir)

        except queue.Empty:
            print("Queue is empty, stopping worker.")
            break

        except Exception as e:
            print(f"Exception occurred while processing {url}: {e}")
import time           
def validate_url(url):
    # Regex pattern for basic URL validation
    url_pattern = re.compile(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    if re.match(url_pattern, url):
        return True
    else:
        return False
def ask():
    
    while True:
        clear_terminal()
        print("\n\nChoose download option:\n")
        print(f"{Fore.YELLOW}1. Download a single websites")
        print(f"{Fore.YELLOW}2. Download multiple websites (up to 10 URLs)")

        choice = input(f"{Fore.CYAN}\n\nEnter your choice (1 or 2): ").strip()

        if choice == '1':
            # Single file download
              clear_terminal()
              while True:
               file_url = input(f"{Fore.MAGENTA}\nEnter the website URL to download: "+Fore.WHITE).strip()
               if validate_url(file_url):
                    return [file_url]                    
                    break
               else:
                    print(f"{Fore.RED}\nInvalid URL format. Please enter a valid URL.")
                    
              break

        elif choice == '2':
            # Mass file download
            clear_terminal()
            file_path = input(f"{Fore.MAGENTA}\nEnter the path to the file containing website URLs: "+Fore.WHITE).strip()
            try:
                with open(file_path, 'r') as f:
                    lines = [line.strip() for line in f if line.strip()]
                    return lines[:10] 
                    #print(start_urls) # Take the first 10 URLs or all if less than 10
                break
            except Exception as e:
                print(f"{Fore.RED}\nError reading file {file_path}: {e}")
                time.sleep(1)
        else:
            print(f"{Fore.RED}\nInvalid choice. Please enter 1 or 2.")
            time.sleep(1)
async def main(max_tasks=500):
    visited = set()
    to_visit = queue.Queue()
    processed_paths = set()
    if (os.path.isdir("spider")):
        pass
    else:
        os.mkdir("spider")
    semaphore = asyncio.Semaphore(max_tasks)
    try:
            start_urls = ask()
            for start_url in start_urls:
                to_visit.put(start_url)
    except Exception as e:
        print(f"{fr}Error {e}")
        return

    async with aiohttp.ClientSession() as session:
        tasks = [worker(session, to_visit, visited, semaphore, processed_paths) for _ in range(max_tasks)]
        clear_terminal()
        await asyncio.gather(*tasks)

    print(f"{fg}Visited {len(visited)} URLs:")
import argparse

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error running main: {e}")

