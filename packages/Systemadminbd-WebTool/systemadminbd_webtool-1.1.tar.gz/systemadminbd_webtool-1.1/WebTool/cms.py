from concurrent.futures import ThreadPoolExecutor 
import random,os
from os import system as alone
from time import time
import requests
yellow = '\033[33m'
green = '\033[32m'
red = '\033[31m'
color_off="\033[0m"       # Text Reset

# Regular Colors
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White

# Bold
bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White

# Underline
ublack="\033[4;30m"       # Black
ured="\033[4;31m"         # Red
ugreen="\033[4;32m"       # Green
uyellow="\033[4;33m"      # Yellow
ublue="\033[4;34m"        # Blue
upurple="\033[4;35m"      # Purple
ucyan="\033[4;36m"        # Cyan
uwhite="\033[4;37m"       # White

# Background
on_black="\033[40m"       # Black
on_red="\033[41m"         # Red
on_green="\033[42m"       # Green
on_yellow="\033[43m"      # Yellow
on_blue="\033[44m"        # Blue
on_purple="\033[45m"      # Purple
on_cyan="\033[46m"        # Cyan
on_white="\033[47m"       # White

# High Intensty
iblack="\033[0;90m"       # Black
ired="\033[0;91m"         # Red
igreen="\033[0;92m"       # Green
iyellow="\033[0;93m"      # Yellow
iblue="\033[0;94m"        # Blue
ipurple="\033[0;95m"      # Purple
icyan="\033[0;96m"        # Cyan
iwhite="\033[0;97m"       # White

# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White
from colorama import init,Fore
import socket,requests
from fake_useragent import UserAgent

init(autoreset=True)
requests.urllib3.disable_warnings()
banne="""
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
    os.system(f"echo \"\"\"{banne}\"\"\" | lolcat")
# Function to read URLs from a file and extract hostnames

# High Intensty backgrounds
on_iblack="\033[0;100m"   # Black
on_ired="\033[0;101m"     # Red
on_igreen="\033[0;102m"   # Green
on_iyellow="\033[0;103m"  # Yellow
on_iblue="\033[0;104m"    # Blue
on_ipurple="\033[10;95m"  # Purple
on_icyan="\033[0;106m"    # Cyan
on_iwhite="\033[0;107m"   # White


line="======================================================"

rl="https://br.com"
def banner():
	clear_terminal()
	import datetime
	os.system(f"echo \"\"\"\t\t\t\t\t  Coded By Systemadminbd\"\"\" | lolcat")
	print("\n\n")

    
def joomla(url,get_source):
	try:
		r=get_source
		if 'content="Joomla!' in r.text or "/index.php?option=com_" in r.text or "/administrator/index.php" in r.text or "/administrator/" in r.text or "/administrator/manifests/files/joomla.xml" in r.text or "/language/en-GB/en-GB.xml" in r.text:
			print(yellow + '[Found Cms Joomla --> ]' + green + url)
			open('cms/joomla.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found Cms Joomla --> ]' + red + url)
	except:
	       pass
        
def laravel1(url,get_source):
	try:
		users = {'User-Agent': UserAgent().random}
		get_source1 = requests.get(url+"/vendor", headers=users, timeout=15).text
		if 'phpunit/' in get_source1 or 'Index of /vendor' in get_source1:
			print(yellow + '[Found Laravel Cookies --> ]' + green + url)
			open('cms/laravel.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found Laravel Cookies --> ]' + red + url)
			joomla(url,get_source)
	except:
		pass
def laravel2(url,get_source):
	try:
		users = {'User-Agent': UserAgent().random}
		get_source1 = requests.get(url+"/.env", headers=users, timeout=15).text
		if 'DB_HOST' in str(get_source1) or 'DB_PASSWORD' in str(get_source1):
			open('cms/env.txt', 'a').write(get_source1+'\n site:'+url+"/.env\n")
			print(yellow + '[Found Laravel Cookies --> ]' + green + url)
			open('cms/laravel.txt', 'a').write(url+'\n')
		else:
			laravel1(url,get_source)
	except:
		pass		
def laravel(url,get_source):
	try:
		if  'X-XSRF-TOKEN' in get_source.cookies and 'XSRF-TOKEN' in get_source.cookies:
			print(yellow + '[Found Laravel Cookies --> ]' + green + url)
			open('cms/laravel.txt', 'a').write(url+'\n')
		else:			
			laravel2(url,get_source)
	except:
		pass

def opencart1(url,get_source):
	try:
		users = {'User-Agent': UserAgent().random}
		get_source1 = requests.get(url+"/admin/view/javascript/common.js", headers=users, timeout=15)
		if  b'getURLVar(key)' in get_source1.text.encode('utf-8'):
			print(yellow + '[Found CMS Opencart --> ]' + green + url)
			open('cms/opencart.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS Opencart--> ]' + red + url)
			laravel(url,get_source)
	except:
		pass
def opencart(url,get_source):
	try:
		if 'index.php?route=common/home' in get_source.cookies:
			print(yellow + '[Found CMS Opencart --> ]' + green + url)
			open('cms/opencart.txt', 'a').write(url+'\n')
		else:
			opencart1(url,get_source)			
	except:
		pass

def drupal1(url,get_source):
	try:
		users = {'User-Agent': UserAgent().random}
		get_source1 = requests.get(url+'/misc/ajax.js', headers=users, timeout=15)
		if b'Drupal.ajax' in get_source1.text.encode('utf-8'):
			print(yellow + '[Found CMS Drupal --> ]' + green + url)
			open('cms/drupal.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS Drupal--> ]' + red + url)
			opencart(url,get_source)
	except:
		pass
def drupal(url,get_source):
	try:
		if 'sites/default' in get_source.cookies:
			print(yellow + '[Found CMS Drupal --> ]' + green + url)
			open('cms/drupal.txt', 'a').write(url+'\n')
		else:
			drupal1(url,get_source)
	except:
		pass
def prestashop(url,get_source):
	try:
		if 'sites/default' in get_source.cookies or b'var prestashop =' in get_source.text.encode('utf-8') or 'content="PrestaShop' in get_source.text:
			print(yellow + '[Found CMS Prestashop --> ]' + green + url)
			open('cms/prestashop.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS Prestashop--> ]' + red + url)
			drupal(url,get_source)
	except:
		pass

def magneto(url,get_source):
	try:
		if 'Mage.Cookies' in get_source.cookies or 'id="login" name="login[password]"' in get_source.text:
			print(yellow + '[Found CMS Magneto --> ]' + green + url)
			open('cms/magneto.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS Magneto--> ]' + red + url)
			prestashop(url,get_source)
	except:
		pass
def vBulletin1(url,get_source):
	try:
		users = {'User-Agent': UserAgent().random}
		get_source1 = requests.get(url+'/js/header-rollup-554.js', headers=users, timeout=15)
		if b"js.compressed/modernizr.min.js" in get_source1.text.encode("utf-8"):
			print(yellow + '[Found CMS vBulletin --> ]' + green + url)
			open('cms/vBulletin.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS vBulletin--> ]' + red + url)
			magneto(url,get_source)
	except Exception as e:
		pass
def vBulletin2(url,get_source):
	try:
		users = {'User-Agent': UserAgent().random}
		get_source2 = requests.get(url+'/images/editor/separator.gi', headers=users, timeout=15)
		if b'GIF89a' in get_source2.text.encode("utf-8"):
			print(yellow + '[Found CMS vBulletin --> ]' + green + url)
			open('cms/vBulletin.txt', 'a').write(url+'\n')
		else:
			vBulletin1(url,get_source)
	except Exception as e:
		pass	
def vBulletin(url,get_source):
	try:
		if 'content="vBulletin' in get_source.text:
			print(yellow + '[Found CMS vBulletin --> ]' + green + url)
			open('cms/vBulletin.txt', 'a').write(url+'\n')
		else:
			vBulletin2(url,get_source)
	except Exception as e:
		pass
def shopify(url,cek):
	try:
		if "_shopify_s" in cek.cookies or "_shopify_y" in cek.cookies or b'https://cdn.shopify.com/shopifycloud/' in cek.text.encode('utf-8') or b'http://cdn.shopify.com/shopifycloud/' in cek.text.encode('utf-8'):
			print(yellow + '[Found Cms shopify --> ]' + green + url)
			open('cms/shopify.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS shopify--> ]' + red + url)
			vBulletin(url,cek)
	except:
			pass			
def wix(url,cek):
	try:
		if "fedops.logger.defaultOverrides" in cek.cookies or "ssr-caching" in cek.cookies:
			print(yellow + '[Found Cms wix --> ]' + green + url)
			open('cms/wix.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS wix--> ]' + red + url)
			shopify(url,cek)
	except:
		pass
def contao(url,cek):
	try:
		if 'content="Contao' in cek.text:
			print(yellow + '[Found Cms contao --> ]' + green + url)
			open('cms/contao.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS contao--> ]' + red + url)
			wix(url,cek)
	except:
		pass
def typo3(url,cek):
	try:
		if 'content="TYPO3' in cek.text or 'href="/typo3conf/ext/' in cek.text or 'typo3conf/ext/' in cek.text or 'typo3temp/assets/' in cek.text or 'href="/typo3temp/assets/' in cek.text:
			print(yellow + '[Found Cms typo3 --> ]' + green + url)
			open('cms/typo3.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS osCommerce--> ]' + red + url)
			contao(url,cek)
	except:
		pass
def hubspot(url,cek):
	try:
		if 'content="HubSpot' in cek.text or '/hs/hsstatic/' in cek.text and '/hs-fs/hub/' in cek.text and '/hs/scriptloader/' in cek.text:
			print(yellow + '[Found Cms hubspot --> ]' + green + url)
			open('cms/hunspot.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS hubspot--> ]' + red + url)
			typo3(url,cek)
	except:
		pass
def squarespace(url,cek):
	try:
		if "crumb"in cek.cookies and "/@sqs/polyfiller/" in cek.text and "/universal/scripts-compressed/" in cek.text or "/universal/styles-compressed/" in cek.text:
			print(yellow + '[Found Cms squarespace --> ]' + green + url)
			open('cms/squarespace.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS squarespace--> ]' + red + url)
			hubspot(url,cek)
	except:
		pass
def osCommerce(url):
	try:
		users = {'User-Agent': UserAgent().random}
		get_source = requests.get(url, headers=users, timeout=15)
		if 'osCommerce' in get_source.cookies:
			print(yellow + '[Found CMS osCommerce --> ]' + green + url)
			open('cms/osCommerce.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS osCommerce--> ]' + red + url)
			squarespace(url,get_source)
	except Exception as e:
		pass
def liferay(url):
	try:
		users = {'User-Agent': UserAgent().random}
		get_source = requests.get(url+'/api/jsonws/invoke', headers=users, timeout=15)
		if b'Unable to deserialize object' in get_source.text.encode('utf-8'):
			print(yellow + '[Found CMS liferay --> ]' + green + url)
			open('cms/liferay.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS liferay--> ]' + red + url)
			osCommerce(url)
	except:
		pass
def telerik1(url):
	try:
		users = {'User-Agent': UserAgent().random}
		get_source = requests.get(url+'/DesktopModules/Admin/RadEditorProvider/DialogHandler.aspx', headers=users, timeout=15)
		if b'Loading the dialog' in get_source.text.encode('utf-8'):
			print(yellow + '[Found CMS telerik --> ]' + green + url)
			open('cms/telerik.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found CMS telerik--> ]' + red + url)
			liferay(url)
	except:
		pass
def telerik2(url):
	try:
		users = {'User-Agent': UserAgent().random}
		get_source = requests.get(url+'/Providers/HtmlEditorProviders/Telerik/Telerik.Web.UI.DialogHandler.aspx', headers=users, timeout=15)
		if b'Loading the dialog' in get_source.text.encode('utf-8'):
			print(yellow + '[Found CMS telerik --> ]' + green + url)
			open('cms/telerik.txt', 'a').write(url+'\n')
		else:
			telerik1(url)
	except:
		pass
def telerik(url):
	try:
		users = {'User-Agent': UserAgent().random}
		get_source = requests.get(url+'/desktopmodules/telerikwebui/radeditorprovider/telerik.web.ui.dialoghandler.aspx', headers=users, timeout=15)
		if b'Loading the dialog' in get_source.text.encode('utf-8'):
			print(yellow + '[Found CMS telerik --> ]' + green + url)
			open('cms/telerik.txt', 'a').write(url+'\n')
		else:
			telerik2(url)
	except Exception as e:
		pass	
def wordpress1(url):
	try:
		users = {'User-Agent': UserAgent().random}
		cek = requests.get(url+'/wp-includes/js/jquery/jquery.js', headers=users, timeout=15)
		if b'(c) jQuery Foundation' in cek.text.encode('utf-8'):
			print(yellow + '[Found Cms Wordpress --> ]' + green + url)
			open('cms/wp.txt', 'a').write(url+'\n')
		else:
			print(yellow + '[Not Found Cms Wordpress --> ]' + red + url)
			telerik(url)
	except:
		pass
def wordpress(url):
	try:
		users = {'User-Agent': UserAgent().random}
		cek = requests.get(url+'/xmlrpc.php?rsd', headers=users, timeout=15)
		if b'WordPress' in cek.text.encode('utf-8'):
			print(yellow + '[Found Cms Wordpress --> ]' + green + url)
			open('cms/wp.txt', 'a').write(url+'\n')
		else:
			wordpress1(url)
	except:
		pass
def add_http(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        wordpress("http://" + url)
    else:   
        wordpress(url)		
def main():
    try:
 	   alone("clear")
 	   banner()
 	   if (os.path.isdir("cms")):
 	       pass
 	   else:
 	       os.mkdir("cms")       
 	   name=str(input(yellow+"[$] Enter file name : "+red))
 	   opens = open(name, mode='r', errors='ignore').read().splitlines()
 	   print(f" Total Url : {len(opens)}")
 	   count_time=time()
 	   with ThreadPoolExecutor(max_workers=100) as abir_is_singel:
 	      abir_is_singel.map(add_http, opens)
 	      abir_is_singel.shutdown(wait=True)
 	   print("--- %s seconds ---" % (time() - count_time))
 	   exit()
    except Exception as e:
    	print(e)
if __name__ == "__main__":
    main()