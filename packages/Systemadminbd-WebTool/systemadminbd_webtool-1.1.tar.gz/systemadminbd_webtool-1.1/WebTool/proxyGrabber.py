import subprocess
import sys
import platform
required_modules = [
    'asyncio', 
    'aiohttp', 
    'datetime', 
    're', 
   # 'lolcat', 
    'base64', 
    'time', 
    'termcolor', 
    'rich', 
    'tqdm'
]

def install_module(module):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])
        print(f"Module '{module}' installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install module '{module}': {e}")





import asyncio
import aiohttp
import datetime
import re
import os
import base64,aiofiles
import time
from termcolor import colored
from rich.progress import track
from tqdm.asyncio import tqdm_asyncio
from rich.console import Console

urls = [
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=all&country=All",
    "https://www.proxy-list.download/api/v1/get?type=socks4",
    "https://api.openproxylist.xyz/socks4.txt",
    "https://openproxy.space/list/socks4",
    "https://proxyspace.pro/socks4.txt",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
    "https://api.openproxylist.xyz/socks5.txt",
    "https://openproxy.space/list/socks5",
    "https://spys.me/socks.txt",
    "https://proxyspace.pro/socks5.txt",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://spys.me/proxy.txt",
    "https://api.openproxylist.xyz/http.txt",
    "http://alexa.lr2b.com/proxylist.txt",
    "http://rootjazz.com/proxies/proxies.txt",
    "https://proxy-spider.com/api/proxies.example.txt",
    "https://multiproxy.org/txt_all/proxy.txt",
    "https://openproxy.space/list/http",
    "https://proxyspace.pro/http.txt",
    "https://proxyspace.pro/https.txt",
    "https://spys.me/proxy.txt",
    "https://www.proxy-list.download/api/v1/get?type=http&anon=elite",
    "https://www.proxy-list.download/api/v1/get?type=http&anon=transparent",
    "https://www.proxy-list.download/api/v1/get?type=http&anon=anonymous",
    "https://spys.me/socks.txt",
    
    #github url
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
        "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
        "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
        "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
        "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
        "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
        "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
        "https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
        "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
        "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
        "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
        "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt",
        "https://github.com/BreakingTechFr/Proxy_Free/blob/main/proxies/all.txt",
        "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/proxylist.txt",
        "https://github.com/MrMarble/proxy-list/blob/main/all.txt",
        "https://github.com/berkay-digital/Proxy-Scraper/blob/main/proxies.txt"
]
urls2= {
   "https://proxylist.geonode.com/api/proxy-list?&limit=500&page={page}": r'"ip":"(\d{1,3}(?:\.\d{1,3}){3})".+?"port":"(\d{1,5})"',
   "https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page={page}": r'<td class="show-ip-div">\s*(\d{1,3}(?:\.\d{1,3}){3})\s*<\/td>\s*<td>\s*<a href="\/\?port=(\d{1,5})">',
  "https://iproyal.com/free-proxy-list/?page={page}&entries=100": r"<div[^>]*>(\d{1,3}(?:\.\d{1,3}){3})<\/div><div[^>]*>(\d{1,5})<\/div>",
   "https://advanced.name/freeproxy?page={page}": (r'data-ip="([^"]+)"', r'data-port="([^"]+)"')
}
banner="""
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗ █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██████╗ ██████╗ 
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██╔══██╗
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║███████║██║  ██║██╔████╔██║██║██╔██╗ ██║██████╔╝██║  ██║
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██╔══██╗██║  ██║
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██████╔╝██████╔╝
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚═════╝"""
async def clear_terminal():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and other Unix-like systems
        os.system('clear')
    os.system(f"echo \"\"\"{banner}\"\"\" | lolcat")
    os.system(f"echo \"\"\"\t\t\t\t\t  Coded By Systemadminbd\"\"\" | lolcat")

async def fetch_url(session, url, semaphore):
    async with semaphore:
        try:
            async with session.get(url, timeout=10) as response:
                return await response.text()
        except Exception as e:
            pass #print(colored(f"URL: {url}, Error: {e}", "red"))
    return ""

def parse_proxies(response_text):
    pattern = re.compile(r"\d{1,3}(?:\.\d{1,3}){3}(?::\d{1,5})?")
    return re.findall(pattern, response_text)

async def check_url(session, url, semaphore):
    response_text = await fetch_url(session, url, semaphore)
    ip_addresses = parse_proxies(response_text)
    if response_text:
        if len(ip_addresses) > 1:
            pass #print(colored(f"URL: {url}, IPs found: {len(ip_addresses)}", "green"))
        else:
            pass #print(colored(f"URL: {url}, IPs found: {len(ip_addresses)}", "blue"))
    else:
        pass #print(colored(f"URL: {url}, No response", "cyan"))
    return ip_addresses

async def opem_proxy_availability(proxy, semaphore):
    async with semaphore:
        try:
            ip, port = proxy.split(":")
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(ip, int(port)), timeout=3)
            writer.close()
            await writer.wait_closed()
            print(colored(f'Proxy: {proxy}, Available: Yes',"green"))
            with open("./good_proxies.txt", "a") as f:
                f.write(proxy+ "\n")
            return proxy, True
        except Exception:
            print(colored(f'Proxy: {proxy}, Available: No',"red"))
            return proxy, False
async def check_proxy_availability(proxy,semaphore):
    async with semaphore:
       try:
        proxy_types = ['http', 'socks4', 'socks5']
        ip, port = proxy.split(":")
        for proxy_type in proxy_types:
            proxy_url = f"{proxy_type}://{ip}:{port}"
            async with aiohttp.ClientSession() as session:
                    async with session.get("http://example.com", proxy=proxy_url, timeout=4) as response:
                        if response.status == 200:
                            print(colored(f'Proxy: {proxy}, Available: Yes',"green"))
                            async with aiofiles.open(f"./{proxy_type}.txt", "a") as file:
                            	await file.write(f"{proxy_type}://{ip}:{port}\n")
                            return proxy, True
       except Exception:
                print(colored(f'Proxy: {proxy}, Available: No',"red"))
                return proxy, False
                     
            
async def fetch_proxies_for_day(session, day, semaphore):
    url = f'https://checkerproxy.net/api/archive/{day.year}-{day.month}-{day.day}'
    response_text = await fetch_url(session, url, semaphore)
    unique_proxies = set()
    if response_text != '[]':                
        new_proxies = parse_proxies(response_text)
        for proxy in new_proxies:
            unique_proxies.add(proxy)
        #print(colored(f"URL: {url}, New IPs found: {len(new_proxies)}", "green"))          
    return list(unique_proxies)
      
                  
                                          
async def get_proxy2(session, url_template, semaphore, pattern):
    page = 1
    seen_proxies = set()
    duplicate_count = 0

    while True:
        url = url_template.format(page=page)
        response_text = await fetch_url(session, url,semaphore)
        if isinstance(pattern, str):
        	proxies=re.findall(pattern, response_text)
        	proxiess=re.findall(pattern, response_text)
        	proxies = []
        	for item in proxiess:
        		if isinstance(item, tuple):
        			ip, port = item
        			proxies.append(f"{ip}:{port}")
        		else:
        			proxies=proxiess        	
        elif isinstance(pattern, tuple):
        	regex_pattern = re.compile(pattern[0] )
        	regex_pattern2=re.compile(pattern[1])
        	prok=regex_pattern.findall(response_text)
        	proxies2=regex_pattern2.findall(response_text)
        	decoded_ips = [base64.b64decode(ip).decode('utf-8') for ip in prok]       	
        	decoded_ports = [base64.b64decode(port).decode('utf-8') for port in proxies2]
        	data=list(zip(decoded_ips, decoded_ports))
        	proxies=[]
        	for ip, port in data:
        		proxies.append(f"{ip}:{port}")
        else:
            raise ValueError("Invalid pattern type")
        if not proxies:
            #print(colored(f"No proxies found at {url}", "cyan"))
            break

        new_proxies = [proxy for proxy in proxies if proxy not in seen_proxies]

        if not new_proxies:
            duplicate_count += 1
            if duplicate_count > 2:  
                #print(colored(f"Stopping due to continuous duplicates at {url}", "yellow"))
                break
        else:
            duplicate_count = 0

        seen_proxies.update(new_proxies)
        #print(colored(f"URL: {url}, New IPs found: {len(new_proxies)}", "green"))
        page += 1

    return list(seen_proxies)

async def scrape_proxies():
    proxies = []
    async def scrape_geonode():
        url = "https://proxylist.geonode.com/api/proxy-list?&limit=500&page=1&sort_by=lastChecked&sort_type=desc"
        async with aiohttp.ClientSession() as session:
            semaphore = asyncio.Semaphore(100)
            response_text = await fetch_url(session, url, semaphore)
            return parse_proxies(response_text)

    async def scrape_proxylistdownload(method, anon):
        url = f"https://www.proxy-list.download/api/v1/get?type={method}&anon={anon}"
        async with aiohttp.ClientSession() as session:
            semaphore = asyncio.Semaphore(100)
            response_text = await fetch_url(session, url, semaphore)
            return parse_proxies(response_text)
            
    proxies += await scrape_geonode()
    proxies += await scrape_proxylistdownload("http", "elite")
    proxies += await scrape_proxylistdownload("http", "transparent")
    proxies += await scrape_proxylistdownload("http", "anonymous")

    async with aiohttp.ClientSession() as session:
        semaphore = asyncio.Semaphore(150)
        
        tasks = []
        
        for url, pattern in urls2.items():
            tasks.append(get_proxy2(session,url,semaphore, pattern))
            
        for q in range(20):
            day = datetime.date.today() + datetime.timedelta(-q)
            task = fetch_proxies_for_day(session, day, semaphore)
            tasks.append(task)
                       
        for url in urls:
        	tasks.append(check_url(session, url, semaphore))      
        	      
            
        #results = await asyncio.gather(*tasks)
        results = await tqdm_asyncio.gather(*tasks, desc="Downloading Proxies")
        for result in results:
            proxies += result

    return proxies

async def main():
    await clear_terminal()
    print("\n")
    for i in track(range(10), description="Starting Program.."):
    	time.sleep(0.1)    	
    print("\n\n")	
    proxies = await scrape_proxies()
    console = Console()

    console.print(f"[bold yellow]\nDownload Finished With Status code: [bold green]OK.\n", style="bold green")
    for i in track(range(10), description="Preparing For Proxy Cheking.."):
    	time.sleep(0.1)
    await clear_terminal()
    console.print("\n[bold cyan]Total Proxies For Cheking : [bold red]"+str(len(proxies)), style="bold blue")
    good_proxies = []

    semaphore = asyncio.Semaphore(450)
    tasks = [check_proxy_availability(proxy, semaphore) for proxy in proxies]
    results = await asyncio.gather(*tasks)
if __name__ == "__main__":
    os_type = platform.system()
    print(f"Detected OS: {os_type}")
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"Module '{module}' is not installed. Installing...")
            install_module(module)
    asyncio.run(main())
