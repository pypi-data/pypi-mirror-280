import asyncio
import aiohttp
import re,os
from colorama import init,Fore
import socket,requests
import fake_useragent
import random
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
# Function to read URLs from a file and extract hostnames

def extract_hostnames_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        hostnames = []
        for line in lines:
            line = line.strip()
            
            # Check if the line is an IP address
            if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', line):
                hostnames.append(line)
            else:
                # Extract hostname from URL
                hostname = re.sub(r'http[s]?://(www\.)?', '', line).split('/')[0]
                hostnames.append(hostname)
            
        return hostnames
    except Exception as e:
        #
        print(e)
        return None

# Example usage:
# print(extract_hostnames_from_file('urls.txt'))

# Asynchronous function to resolve hostname to IP address
async def get_ip_from_hostname(hostname):
    loop = asyncio.get_event_loop()
    try:
       if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', hostname):
           return hostname
       else:       
        infos = await loop.getaddrinfo(hostname, None, proto=socket.IPPROTO_TCP)
        return infos[0][4][0]
    except socket.gaierror:
        return None
    except Exception as e:
        #print(f"Error resolving hostname {hostname}: {e}")
        return None

# Function to get random headers
def get_random_headers():

    accept_langs = ["en-US,en;q=0.5", "en-GB,en;q=0.9", "en-AU,en;q=0.8", "en-CA,en;q=0.7"]
    accepts = ["text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"]
    encodings = ["gzip, deflate, br", "gzip, deflate", "br, gzip, deflate"]
    referers = ["https://www.google.com/", "https://www.bing.com/", "https://www.yahoo.com/", "https://www.duckduckgo.com/"]
    accept_charset = ["ISO-8859-1,utf-8;q=0.7,*;q=0.7", "ISO-8859-1,utf-8;q=0.7,*;q=0.7", "utf-8;q=0.7,*;q=0.7,ISO-8859-1", "utf-8;q=0.7,*;q=0.7"]
    cache_controls = ["no-cache", "no-store", "max-age=0", "max-age=3600"]

    headers = {
        "User-Agent": fake_useragent.UserAgent().random,
        "Accept": random.choice(accepts),
        "Accept-Language": random.choice(accept_langs),
        "Accept-Encoding": random.choice(encodings),
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Referer": random.choice(referers),
        "Accept-Charset": random.choice(accept_charset),
        "Cache-Control": random.choice(cache_controls),
        "X-Requested-With": "XMLHttpRequest"
    }
    return headers

# Function to get proxies
def get_proxy():
    import requests
    import re

    try:
        proxies = []
        for proxy_type in ["http", "socks4"]:
            res = requests.get(f"https://api.proxyscrape.com/?request=displayproxies&proxytype={proxy_type}&country=all")
            pattern = re.compile(r"\d{1,3}(?:\.\d{1,3}){3}(?::\d{1,5})?")
            proxies.extend([f"{proxy_type}://{proxy}" for proxy in re.findall(pattern, res.text)])
        return proxies
    except:
        return []

# Asynchronous function to fetch data using a random proxy
async def fetch_data_with_random_proxy(session, url, proxies, semaphore):
    import random

    async with semaphore:
        selected_proxy = random.choice(proxies)
        proxy = f"{selected_proxy}"  # Ensure proxy URL format is correct
        headers = get_random_headers()

        try:
            async with session.get(url, proxy=proxy, headers=headers) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return None
        except Exception as e:
            #print(f"Exception fetching URL {url} with proxy {proxy}: {e}")
            # If proxy fails, retry without proxy
            try:
                async with session.get(url, headers=headers) as response:
                    #print(response.status)
                    if response.status == 200:
                        return await response.text()
                    else:
                        return None
            except Exception as e:
                #print(f"Exception fetching URL {url} without proxy: {e}")
                return None

# Asynchronous function to process a single domain name
async def process_domain(ip, session, semaphore, proxies, unique_domains):
    url = f'https://rapiddns.io/s/{ip}?full=1&down=1#result'
    html_content = await fetch_data_with_random_proxy(session, url, proxies, semaphore)

    if html_content and '<th scope="row ">' in html_content:
        regex = re.findall('<td>(?!-)(?:[a-zA-Z\\d-]{0,62}[a-zA-Z\\d].){1,126}(?!\\d+)[a-zA-Z]{1,63}</td>', html_content)
        domains = [domain.replace('<td>', '').replace('</td>', '').strip() for domain in regex]

        for domain in domains:
            if domain not in unique_domains and not re.match(r'^\d{1,3}(\.\d{1,3}){3}$', domain) and not domain.endswith(('htm', 'html')) and 'piliang' not in domain:
                print(f"{Fore.GREEN}http://{domain}")
                with open("./revUrl.txt", "a") as f:
                                f.writelines((f"http://{domain}\n"))
                unique_domains.add(domain)
    else:
        pass
        #print(f"Failed to retrieve data or no domains found for IP: {ip}")

# Asynchronous function to resolve hostnames and process domains concurrently
async def resolve_and_process(hostname_queue, session, semaphore, proxies, unique_domains):
    while True:
        hostname = await hostname_queue.get()
        if hostname is None:
            break
        ip = await get_ip_from_hostname(hostname)
        if ip:
            await process_domain(ip, session, semaphore, proxies, unique_domains)
        hostname_queue.task_done()

# Main function to coordinate everything
async def main():
              try:
               clear_terminal()
               os.system(f"echo \"\"\"\t\t\t\t\t  Coded By Systemadminbd\"\"\" | lolcat")
               filename =str(input("\n\033[1;92mEnter url list [it will convert domain to ip automatically] : "))
               print(" \n\n")
                
               hostnames = extract_hostnames_from_file(filename)
               if hostnames:             
                semaphore = asyncio.Semaphore(100)  # Limit to 100 concurrent requests
                proxies = get_proxy()
            
                unique_domains = set()
                hostname_queue = asyncio.Queue()
            
                for hostname in hostnames:
                    await hostname_queue.put(hostname)
            
                async with aiohttp.ClientSession() as session:
                    workers = [asyncio.create_task(resolve_and_process(hostname_queue, session, semaphore, proxies, unique_domains)) for _ in range(100)]
                    
                    await hostname_queue.join()
            
                    for _ in range(100):
                        await hostname_queue.put(None)
            
                    await asyncio.gather(*workers)
              except Exception as e:
                   print(e)
                   pass
# Run the main function
if __name__ == "__main__":
      asyncio.run(main())