import asyncio
import aiohttp,requests
from bs4 import BeautifulSoup
import random,os,time
from urllib.parse import urlparse, urlunparse
import fake_useragent
from colorama import init,Fore
init(autoreset=True)
requests.urllib3.disable_warnings()
from urllib.parse import quote as quote_url, unquote as unquote_url
import json
import re

BASE_URL_DUCKDUCKGO = 'https://html.duckduckgo.com'
BASE_URL_YAHOO = 'https://search.yahoo.com'
BASE_URL_QWANT = 'https://api.qwant.com/v3/search/web'
BASE_URL_GOOGLE = 'https://www.google.com'
BASE_URL_AOL = 'https://search.aol.com'
FAKE_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
dom = ['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'za', 'zm', 'zw', 'com', 'net', 'org', 'biz', 'gov', 'mil', 'edu', 'info', 'int', 'tel', 'name', 'aero', 'asia', 'cat', 'coop', 'jobs', 'mobi', 'museum', 'pro', 'travel']  # Your list of domains
banner="""
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗ █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██████╗ ██████╗ 
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██╔══██╗
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║███████║██║  ██║██╔████╔██║██║██╔██╗ ██║██████╔╝██║  ██║
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██╔══██╗██║  ██║
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██████╔╝██████╔╝
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚═════╝"""
dork=False
def clear_terminal():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and other Unix-like systems
        os.system('clear')
    os.system(f"echo \"\"\"{banner}\"\"\" | lolcat")
    os.system(f"echo \"\"\"\t\t\t\t\t  Coded By Systemadminbd\"\"\" | lolcat")
    print("\n\n")
sub_domain=""
async def chose_domain():
    while True:
    	clear_terminal()
    	print(dom)
    	domain=str(input(Fore.WHITE+"\n\nEnter sub domain : "))
    	if domain in dom:
    		print(" \nYour sub domain ",domain)
    		sub_domain="site:."+domain
    		break
    	elif domain == "" or domain==" ":
    		print(Fore.RED+"no sub domain inputed we will use defualt domin")
    		time.sleep(1)
    		os.system('clear')
    		sub_domain=""
    		break		
    	else:
    		pass

# Array of popular website names
popular_websites = ['http://fiver.com','http://linkedin.com','http://github.com','http://google.com','http://facebook.com','http://go.microsoft.com','http://#']

# Array of queries

queries = []
querie=[]
async def get_bing_suggestions(keyword, session):
    url = f"https://api.bing.com/osjson.aspx?query={keyword}"
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            suggestions = (await response.json())[1]
            for suggestion in suggestions:
                if suggestion not in queries:
                    queries.append(suggestion)
                #print(suggestion)
          
    except aiohttp.ClientError as e:
        pass

def generate_keyword_combinations_helper(keywords, current_combination, index, result_set):
    result_set.add(" ".join(current_combination))

    for i in range(index, len(keywords)):
        generate_keyword_combinations_helper(keywords, current_combination + [keywords[i]], i + 1, result_set)

def generate_keyword_combinations(keywords):
    result_set = set()

    generate_keyword_combinations_helper(keywords, [], 0, result_set)

    for unique_combination in result_set:
        if not unique_combination in querie:
        	querie.append(unique_combination)

async def chose_keyword():
    clear_terminal()     	  
    while True:
        user_input = input(Fore.YELLOW+"\nEnter a Keyword, maximum 5 words: ")
        
        if user_input == "":
            print(Fore.CYAN+"\nPlease enter SEO keywords.")
        elif len(user_input.split()) <= 5:
            print(Fore.WHITE+"\nMaximum 5 words received. Adding to queries list.")
            querie.extend(user_input.split()[:5])                
            #strart_suggetion_grab()
            break
        else:
            print(Fore.RED+"\nMore than 5 words received. Taking the first 5 words.")
            querie.extend(user_input.split()[:5])
            #strart_suggetion_grab()
            break
# Set to store processed URLs
# Get a Keyword From The User
async def strart_suggetion_grab():
       try:
        await chose_domain()
        await chose_keyword()
        generate_keyword_combinations(querie)
        async with aiohttp.ClientSession() as session:
        	for keyword in querie:        	 
          	  await get_bing_suggestions(keyword, session)
       except Exception as e:
           pass #print(e)          	  
#os.system("clear")
processed_urls = set()
counter=0
async def dork_method():
    dork_file = str(input("\033[1;32m\nEnter your dork file path :\033[1;33m "))
    try:
        with open(dork_file, 'r') as file:
            tasks = []
            for line in file.read().splitlines():
                queries.append(line)
 
    except FileNotFoundError:
        print("\033[1;31mDork file not found. Please try again.\033[0m")


async def chose_option():
    while True:
        print("\033[1;92mChoose an option:\033[0m\n")
        print("\033[1;94m1. Keyword Method\033[0m")
        print("\033[1;94m2. Dork Method\033[0m")
        choice = input("\n\033[1;96mEnter your choice (1 or 2): \033[0m")
        if choice == '1':
            await strart_suggetion_grab()
            break
        elif choice == '2':
            clear_terminal()
            global dork
            dork=True
            await dork_method()
            break
        else:
            print("\033[1;31mInvalid choice. Please choose 1 or 2.\033[0m")
async def fetch(url,session):
    
        try:
            headers = {'user-agent': fake_useragent.UserAgent().random}
            async with session.get(url, timeout=10,headers=headers) as response:
                response.raise_for_status()  # Raise exception for non-2xx responses
                return await response.text()
        except aiohttp.ClientError as e:
            print(f"Error fetching {url}: {e}")
            return None
        except Exception as e:
            #print(e)
            return None


def normalize_url(url):
    parsed_url = urlparse(url)
    return urlunparse((parsed_url.scheme, parsed_url.netloc, "", "", "", ""))
def get_random_headers():
    import fake_useragent
    import random

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
            async with session.get(url, proxy=proxy,timeout=10, headers=headers) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return None
        except Exception as e:
            ##print(f"Exception fetching URL {url} with proxy {proxy}: {e}")
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


async def procesed(url):
   if url not in popular_websites:
    global counter
    counter=counter+1
    print(f"{Fore.MAGENTA}[{str(counter)}] {Fore.WHITE}==>{Fore.GREEN} {url} ")
    with open("./url.txt", "a") as f:
        f.writelines(url + "\n")    
async def ho(bing, query, semaphore,proxies):
    async with semaphore:
       async with aiohttp.ClientSession() as session:
        #html = await fetch(bing,session)
        html=await fetch_data_with_random_proxy(session, bing, proxies, semaphore)
        #print(html)
        if html is None:
            return True  # Skip processing on fetch error

        try:
            soup = BeautifulSoup(html, "lxml")
            if "No results found" in soup.text:
                pass
                return True  # Signal to break out of alldomains loop

            for i in soup.findAll('a', attrs={"h": True}):
                try:
                    if "http" in i["href"]:
                        url = normalize_url("http://" + str(i["href"]).split("/")[2])
                        if "http://search" not in url and \
                           url not in processed_urls and \
                           not any(website in url for website in popular_websites) and \
                           all(keyword not in url for keyword in ["microsoft", "bing"]):
                            await procesed(url)                              
                            processed_urls.add(url)
                except IndexError:
                    print('index error')
                    pass  # Handle the IndexError and continue with the loop

        except Exception as e:
            print(e)
            pass
            # Handle other exceptions if needed

    return False  # Continue with alldomains loop


async def parse_urls_from_html(status,html, url_selector, domain_regex):
    soup = BeautifulSoup(html, 'html.parser')
    for result in soup.select(url_selector):
        url = result.get('href')        
        if url:
            match = re.match(domain_regex, url)
            if match:
                domain = "http://"+match.group(1)
                if domain not in processed_urls:
                    await procesed(domain)#print(f"[{status}] : http://"+str(domain))
                    processed_urls.add(domain)


def get_next_page_url(html, next_page_selector):
    soup = BeautifulSoup(html, 'html.parser')
    next_page = soup.select_one(next_page_selector)
    if next_page:
        return BASE_URL_DUCKDUCKGO + next_page['href'] if 'duckduckgo' in next_page_selector else next_page['href']
    return None

async def search_duckduckgo(query,semaphore,proxies):
    async with aiohttp.ClientSession() as session:
        url = f"{BASE_URL_DUCKDUCKGO}/html/?q={quote_url(query)}"
        while url:
            html = await fetch_data_with_random_proxy(session, url, proxies, semaphore)
            if not html:
                break
            await parse_urls_from_html("DuckDuckGo",html, 'a.result__a', r'^(?:https?://)?(?:www\.)?([^/]+)')
            url = get_next_page_url(html, 'input[value="next"]')
async def parse_yahoo_urls_from_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    for result in soup.select('div#web li div.dd.algo.algo-sr div.compTitle h3.title a'):
        url = result.get('href')
       
        if url:
            url = url.split('/RU=')[-1].split('/R')[0]
            url = unquote_url(url)
            domain_pattern=re.compile(r'^(?:https?://)?([^/]+)')
            match=domain_pattern.match(url)
            if url not in processed_urls and match:
                url="http://"+match.group(1)
                processed_urls.add(url)
                await procesed(url)#print("[Yahoo] : http://"+url)

async def search_yahoo(query,semaphore,proxies):
    async with aiohttp.ClientSession() as session:
        url = f"{BASE_URL_YAHOO}/search?p={quote_url(query)}&ei=UTF-8&nojs=1"
        while url:
            html = await fetch_data_with_random_proxy(session, url, proxies, semaphore)
            if not html:
                break
            await parse_yahoo_urls_from_page(html)
            url = get_next_page_url(html, 'a.next')

async def search_qwant(query,semaphore,proxies):
    offset = 0
    async with aiohttp.ClientSession() as session:
        while offset < 50:
            url = f"{BASE_URL_QWANT}?q={quote_url(query)}&count=10&locale=en_US&offset={offset}&device=desktop&safesearch=1"
            html = await fetch_data_with_random_proxy(session, url, proxies, semaphore)
            if not html:
                break
            data = json.loads(html)
            for item in data.get('data', {}).get('result', {}).get('items', {}).get('mainline', []):
                for sub_item in item.get('items', []):
                    if sub_item.get('type') != 'ads':
                        url = sub_item.get('url')
                        if url:
                            domain = re.match(r'^(?:https?://)?(?:www\.)?([^/]+)', url)
                            if domain:
                                domain_name = "http://"+domain.group(1)
                                if domain_name not in processed_urls:
                                    await procesed(domain_name)#print("[Qwant] : http://"+domain_name)
                                    processed_urls.add(domain_name)
            offset += 10

async def search_google(query,semaphore,proxies):
   async with aiohttp.ClientSession() as session:
    offset = 0
    while True:
        url = f"{BASE_URL_GOOGLE}/search?q={quote_url(query)}&start={offset}"          
        html = await fetch_data_with_random_proxy(session, url, proxies, semaphore)
        if not html:
            break
        await parse_urls_from_html("[Google]",html, 'a[href]', r'^(?:https?://)?(?:www\.)?([^/]+)')
        url = get_next_page_url(html, 'footer a[href][aria-label="Next page"]')
        if not url:
            break
        offset += 10
async def parse_aol_urls_from_page(html,domain_pattern=re
.compile(r'^(?:(?:https?://)?(?:www\.)?)?([^/]+\.[^/]+)$')):
    soup = BeautifulSoup(html, 'html.parser')
    for result in soup.select('span'):
        text = result.get_text(strip=True).strip()
        if ' ' in text or '(' in text or ')' in text:
            continue
        if text:
            match = domain_pattern.match(text)
            if match:
                domain_name = "http://"+match.group(1)
                if domain_name not in processed_urls:
                    await procesed(domain_name)#print(f"[Aol] : http://{domain_name}")
                    processed_urls.add(domain_name)
async def search_aol(query,semaphore,proxies):
    async with aiohttp.ClientSession() as session:
        url = f"{BASE_URL_AOL}/aol/search?q={quote_url(query)}&ei=UTF-8&nojs=1"
        while url:
            #html = await fetch_page(url, session)
            html = await fetch_data_with_random_proxy(session, url, proxies, semaphore)
            if not html:
                break
            await parse_aol_urls_from_page(html)
            url = get_next_page_url(html, 'a.next')

async def alldomains():
    try:
        proxies=get_proxy()
        semaphore = asyncio.Semaphore(300)  # Adjust the number of concurrent requests as needed

        if dork:
            print(Fore.GREEN + "Wait Processing your Dorks.....\n\n")
            page_limit = 100
        else:
            print(Fore.GREEN + "Wait Processing your Keywords.....\n\n")
            page_limit = 2000

        tasks = []
        for query in queries:
            func= [
        search_duckduckgo(query,semaphore,proxies),
       search_yahoo(query,semaphore,proxies),
       search_qwant(query,semaphore,proxies),
       search_aol(query,semaphore,proxies),
       search_google(query,semaphore,proxies)
    ]
            for task in func:
                    tasks.append(task)
            for page in range(0, page_limit, 10):  # Adjust the range based on your needs
                bing = (f"https://www.bing.com/search?q={query} {sub_domain}&qs=n&sp=-1&lq=0&pq={query} "
                        f"{sub_domain}&sc=2-11&sk=&cvid=6BA446DA2B9A4FD9B151375419345F2D&ghsh=0&ghacc=0&ghpl=&FPIG="
                        f"48E4915EE2F44B15B8AE40C2CDD6D818&count=50&setlang=en&safesearch=off&first={page}&FORM=PORE")
                task=ho(bing, query, semaphore,proxies)
                tasks.append(task)

        # Run tasks asynchronously
        await asyncio.gather(*tasks)
    except Exception as e:
        print(e)



async def main():
    clear_terminal()
    await chose_option()
    clear_terminal()
    await alldomains()

if __name__ == "__main__":
    asyncio.run(main())

