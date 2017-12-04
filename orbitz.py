from selenium import webdriver as wd
import sys, time, re, argparse
reload(sys)
sys.setdefaultencoding('utf-8')

site = 'orbitz'
results = 30
num_block = 10
agents = 4	#use only even numbers
browsers = []
profiles = []
locations = []

parser = argparse.ArgumentParser()
parser.add_argument("--usa", help="compare two usa cities", action="store_true")
parser.add_argument("--taiwan", help="compare two taiwan cities", action="store_true")
parser.add_argument("--indonesia", help="compare two indonesia cities", action="store_true")
parser.add_argument("--brazil", help="compare two brazil cities", action="store_true")
parser.add_argument("--china", help="compare two china cities", action="store_true")
parser.add_argument("--germany", help="compare two germany cities", action="store_true")
parser.add_argument("--usa_vs_indo", help="compare two countries usa and indonesia", action="store_true")
args = parser.parse_args()

if args.usa:
    location = ['AH','LA'] #use sorted list, number of cities are fixed
    country = 'usa'
elif args.taiwan:
    location = ['hsinchu','taipei'] #use sorted list, number of cities are fixed
    country = 'taiwan'
elif args.indonesia:
    location = ['jakarta','makasser'] #use sorted list, number of cities are fixed
    country = 'indonesia'
elif args.germany:
    location = ['baden','kiez'] #use sorted list, number of cities are fixed
    country = 'germany'
elif args.china:
    location = ['beijing','nanning'] #use sorted list, number of cities are fixed
    country = 'china'
elif args.brazil:
    location = ['osasco','parana'] #use sorted list, number of cities are fixed
    country = 'brazil'
elif args.usa_vs_indo:
    location = ['indonesia','usa'] #use sorted list
    country = 'usa_vs_indonesia'
else:
    parser.print_help()
    sys.exit(1)	

for l in range(agents/2):
    browser = 'browser' + str(l+1)
    browsers.append(browser)
    browser = 'browser' + str(l+3)
    browsers.append(browser)
    locations.append(location[0])
    locations.append(location[1])
    profile = 'profile' + str(l+1)
    profiles.append(profile)
    profile = 'profile' + str(l+3)
    profiles.append(profile)
profiles.sort()    
browsers.sort()
locations.sort()

f = open(site + '_' + country + '.txt','wb')

for i in range(num_block):
    print site + ' ' + country + ' block ' + str(i+1) + ' started'   
    if args.usa:
        for k in range(agents/2):
            profiles[k] = wd.FirefoxProfile()
            profiles[k].set_preference("network.proxy.type", 1)
            profiles[k].set_preference("network.proxy.https", "35.201.253.111")
            profiles[k].set_preference("network.proxy.https_port", "3218")
            profiles[k].set_preference("dom.disable_beforeunload", True)
            profiles[k].set_preference("dom.popup_maximum", 0)
            profiles[k].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k].set_preference("browser.cache.disk.enable", False)
            profiles[k].set_preference("browser.cache.memory.enable", False)
            profiles[k].set_preference("browser.cache.offline.enable", False)
            profiles[k].set_preference("network.http.use-cache", False)
            profiles[k].update_preferences()

            profiles[k+2] = wd.FirefoxProfile()
            profiles[k+2].set_preference("network.proxy.type", 1)
            profiles[k+2].set_preference("network.proxy.https", "174.138.54.111")
            profiles[k+2].set_preference("network.proxy.https_port", "3218")
            profiles[k+2].set_preference("dom.disable_beforeunload", True)
            profiles[k+2].set_preference("dom.popup_maximum", 0)
            profiles[k+2].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k+2].set_preference("browser.cache.disk.enable", False)
            profiles[k+2].set_preference("browser.cache.memory.enable", False)
            profiles[k+2].set_preference("browser.cache.offline.enable", False)
            profiles[k+2].set_preference("network.http.use-cache", False)
            profiles[k+2].update_preferences()
            
    elif args.taiwan:
        #set firefox profiles
        for k in range(agents/2):
            profiles[k] = wd.FirefoxProfile()
            profiles[k].set_preference("network.proxy.type", 1)
            profiles[k].set_preference("network.proxy.https", "211.79.61.8")
            profiles[k].set_preference("network.proxy.https_port", "3128")
            profiles[k].set_preference("dom.disable_beforeunload", True)
            profiles[k].set_preference("dom.popup_maximum", 0)
            profiles[k].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k].set_preference("browser.cache.disk.enable", False)
            profiles[k].set_preference("browser.cache.memory.enable", False)
            profiles[k].set_preference("browser.cache.offline.enable", False)
            profiles[k].set_preference("network.http.use-cache", False)
            profiles[k].update_preferences()

            profiles[k+2] = wd.FirefoxProfile()
            profiles[k+2].set_preference("network.proxy.type", 1)
            profiles[k+2].set_preference("network.proxy.https", "61.216.24.97")
            profiles[k+2].set_preference("network.proxy.https_port", "3128")
            profiles[k+2].set_preference("dom.disable_beforeunload", True)
            profiles[k+2].set_preference("dom.popup_maximum", 0)
            profiles[k+2].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k+2].set_preference("browser.cache.disk.enable", False)
            profiles[k+2].set_preference("browser.cache.memory.enable", False)
            profiles[k+2].set_preference("browser.cache.offline.enable", False)
            profiles[k+2].set_preference("network.http.use-cache", False)
            profiles[k+2].update_preferences()

    elif args.indonesia:
        #set firefox profiles
        for k in range(agents/2):
            profiles[k] = wd.FirefoxProfile()
            profiles[k].set_preference("network.proxy.type", 1)
            profiles[k].set_preference("network.proxy.https", "36.67.108.53")
            profiles[k].set_preference("network.proxy.https_port", "62225")
            profiles[k].set_preference("dom.disable_beforeunload", True)
            profiles[k].set_preference("dom.popup_maximum", 0)
            profiles[k].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k].set_preference("browser.cache.disk.enable", False)
            profiles[k].set_preference("browser.cache.memory.enable", False)
            profiles[k].set_preference("browser.cache.offline.enable", False)
            profiles[k].set_preference("network.http.use-cache", False)
            profiles[k].update_preferences()

            profiles[k+2] = wd.FirefoxProfile()
            profiles[k+2].set_preference("network.proxy.type", 1)
            profiles[k+2].set_preference("network.proxy.https", "202.124.205.26")
            profiles[k+2].set_preference("network.proxy.https_port", "3128")
            profiles[k+2].set_preference("dom.disable_beforeunload", True)
            profiles[k+2].set_preference("dom.popup_maximum", 0)
            profiles[k+2].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k+2].set_preference("browser.cache.disk.enable", False)
            profiles[k+2].set_preference("browser.cache.memory.enable", False)
            profiles[k+2].set_preference("browser.cache.offline.enable", False)
            profiles[k+2].set_preference("network.http.use-cache", False)
            profiles[k+2].update_preferences()

    elif args.germany:
        #set firefox profiles
        for k in range(agents/2):
            profiles[k] = wd.FirefoxProfile()
            profiles[k].set_preference("network.proxy.type", 1)
            profiles[k].set_preference("network.proxy.https", "149.172.246.81")
            profiles[k].set_preference("network.proxy.https_port", "3218")
            profiles[k].set_preference("dom.disable_beforeunload", True)
            profiles[k].set_preference("dom.popup_maximum", 0)
            profiles[k].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k].set_preference("browser.cache.disk.enable", False)
            profiles[k].set_preference("browser.cache.memory.enable", False)
            profiles[k].set_preference("browser.cache.offline.enable", False)
            profiles[k].set_preference("network.http.use-cache", False)
            profiles[k].update_preferences()

            profiles[k+2] = wd.FirefoxProfile()
            profiles[k+2].set_preference("network.proxy.type", 1)
            profiles[k+2].set_preference("network.proxy.https", "138.201.51.141")
            profiles[k+2].set_preference("network.proxy.https_port", "3218")
            profiles[k+2].set_preference("dom.disable_beforeunload", True)
            profiles[k+2].set_preference("dom.popup_maximum", 0)
            profiles[k+2].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k+2].set_preference("browser.cache.disk.enable", False)
            profiles[k+2].set_preference("browser.cache.memory.enable", False)
            profiles[k+2].set_preference("browser.cache.offline.enable", False)
            profiles[k+2].set_preference("network.http.use-cache", False)
            profiles[k+2].update_preferences()

    elif args.china:    
        #set firefox profiles
        for k in range(agents/2):
            profiles[k] = wd.FirefoxProfile()
            profiles[k].set_preference("network.proxy.type", 1)
            profiles[k].set_preference("network.proxy.https", "61.160.208.222")
            profiles[k].set_preference("network.proxy.https_port", "8080")
            profiles[k].set_preference("dom.disable_beforeunload", True)
            profiles[k].set_preference("dom.popup_maximum", 0)
            profiles[k].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k].set_preference("browser.cache.disk.enable", False)
            profiles[k].set_preference("browser.cache.memory.enable", False)
            profiles[k].set_preference("browser.cache.offline.enable", False)
            profiles[k].set_preference("network.http.use-cache", False)
            profiles[k].update_preferences()

            profiles[k+2] = wd.FirefoxProfile()
            profiles[k+2].set_preference("network.proxy.type", 1)
            profiles[k+2].set_preference("network.proxy.https", "116.11.254.37")
            profiles[k+2].set_preference("network.proxy.https_port", "80")
            profiles[k+2].set_preference("dom.disable_beforeunload", True)
            profiles[k+2].set_preference("dom.popup_maximum", 0)
            profiles[k+2].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k+2].set_preference("browser.cache.disk.enable", False)
            profiles[k+2].set_preference("browser.cache.memory.enable", False)
            profiles[k+2].set_preference("browser.cache.offline.enable", False)
            profiles[k+2].set_preference("network.http.use-cache", False)
            profiles[k+2].update_preferences()

    elif args.brazil:
        #set firefox profiles
        for k in range(agents/2):
            profiles[k] = wd.FirefoxProfile()
            profiles[k].set_preference("network.proxy.type", 1)
            profiles[k].set_preference("network.proxy.https", "177.8.169.254")
            profiles[k].set_preference("network.proxy.https_port", "3128")
            profiles[k].set_preference("dom.disable_beforeunload", True)
            profiles[k].set_preference("dom.popup_maximum", 0)
            profiles[k].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k].set_preference("browser.cache.disk.enable", False)
            profiles[k].set_preference("browser.cache.memory.enable", False)
            profiles[k].set_preference("browser.cache.offline.enable", False)
            profiles[k].set_preference("network.http.use-cache", False)
            profiles[k].update_preferences()

            profiles[k+2] = wd.FirefoxProfile()
            profiles[k+2].set_preference("network.proxy.type", 1)
            profiles[k+2].set_preference("network.proxy.https", "189.115.92.71")
            profiles[k+2].set_preference("network.proxy.https_port", "80")
            profiles[k+2].set_preference("dom.disable_beforeunload", True)
            profiles[k+2].set_preference("dom.popup_maximum", 0)
            profiles[k+2].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k+2].set_preference("browser.cache.disk.enable", False)
            profiles[k+2].set_preference("browser.cache.memory.enable", False)
            profiles[k+2].set_preference("browser.cache.offline.enable", False)
            profiles[k+2].set_preference("network.http.use-cache", False)
            profiles[k+2].update_preferences()

    elif args.usa_vs_indo:
        #set firefox profiles       
        for k in range(agents/2):
            profiles[k] = wd.FirefoxProfile()
            profiles[k].set_preference("network.proxy.type", 1)
            profiles[k].set_preference("network.proxy.https", "202.124.205.26")
            profiles[k].set_preference("network.proxy.https_port", "3128")
            profiles[k].set_preference("dom.disable_beforeunload", True)
            profiles[k].set_preference("dom.popup_maximum", 0)
            profiles[k].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k].set_preference("browser.cache.disk.enable", False)
            profiles[k].set_preference("browser.cache.memory.enable", False)
            profiles[k].set_preference("browser.cache.offline.enable", False)
            profiles[k].set_preference("network.http.use-cache", False)
            profiles[k].update_preferences()

            profiles[k+2] = wd.FirefoxProfile()
            profiles[k+2].set_preference("network.proxy.type", 1)
            profiles[k+2].set_preference("network.proxy.https", "174.138.54.111")
            profiles[k+2].set_preference("network.proxy.https_port", "3218")
            profiles[k+2].set_preference("dom.disable_beforeunload", True)
            profiles[k+2].set_preference("dom.popup_maximum", 0)
            profiles[k+2].set_preference("privacy.popups.showBrowserMessage", False)
            profiles[k+2].set_preference("browser.cache.disk.enable", False)
            profiles[k+2].set_preference("browser.cache.memory.enable", False)
            profiles[k+2].set_preference("browser.cache.offline.enable", False)
            profiles[k+2].set_preference("network.http.use-cache", False)
            profiles[k+2].update_preferences()

    for h in range(agents):
        browsers[h] = wd.Firefox(firefox_profile=profiles[h])
        browsers[h].set_window_position(0, 0)
        browsers[h].set_window_size(560, 280)
        browsers[h].get('https://www.orbitz.com/Hotel-Search?#&destination=Singapore%20(all)%2C%20Singapore&startDate=12/12/2017&endDate=12/30/2017&regionId=180027&latLong=1.290270,103.852010&adults=2') #go to site
        default = browsers[h].window_handles[0] #get the handle number for default window`
        #print 'browser handle is: ' + str(default)
        browsers[h].switch_to.window(default)
        #print 'current url is: ' + str(browser1.current_url)	
        time.sleep(5)

    for m in range(agents):
        num_results = 0
        print 'Agent' + str(m+1) + ' started block ' + str(i+1) + ' ' + str(locations[m])
        prices = browsers[m].find_elements_by_xpath('//article[@id]')
        products = prices
        for price,product in map(None, prices, products):        
            if num_results < results:
                new_product = product.text
                new_product,sep,tail = new_product.partition('\n')
                new_product = re.sub(',', ' ', new_product)
                new_price = price.text                
                if 'Price is now:' in new_price:
                    head,sep,new_price = new_price.partition('Price is now:')
                    new_price,sep,tail = new_price.partition('Price is')
                    
                elif 'This crossed out price reflects the standard hotel rate.'	in new_price:
                    head,sep,new_price = new_price.partition('This crossed out price reflects the standard hotel rate.')
                    new_price,sep,tail = new_price.partition('Price is')
                new_price = re.sub('[^0-9\.]', '', new_price)
                num_results = num_results+1    
                f.write('%s,%d,%d,%d,%s,%s\n'%(locations[m],i+1,m+1,num_results,new_product,new_price))    
        print 'Agent' + str(m+1) + ' done block ' + str(i+1) + ' ' + str(locations[m])

    for x in range(agents):    
        browsers[x].quit()
    print site + ' ' + country + ' block ' + str(i+1) + ' completed'
f.close()
