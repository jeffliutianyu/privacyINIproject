from selenium import webdriver as wd
import sys, re, time, argparse
reload(sys)
sys.setdefaultencoding('utf-8')

# NOTE: For ebay, we take the product id instead of product name due to repeated product name

site = 'ebay'
search = 'back support'
num_block = 10
results = 30
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
    location = ['AH','LA'] #use sorted list, number of cities fixed
    country = 'usa'
elif args.taiwan:
    location = ['hsinchu','taipei'] #use sorted list, number of cities fixed
    country = 'taiwan'
elif args.indonesia:
    location = ['jakarta','makasser'] #use sorted list, number of cities fixed
    country = 'indonesia'
elif args.germany:
    location = ['baden','kiez'] #use sorted list, number of cities fixed
    country = 'germany'
elif args.china:
    location = ['beijing','nanning'] #use sorted list, number of cities fixed
    country = 'china'
elif args.brazil:
    location = ['osasco','parana'] #use sorted list, number of cities fixed
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

#open files to write
f = open(site + '_' + country + '.txt', 'wb')

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
        
    #set browser profiles
    for h in range(agents):
        browsers[h] = wd.Firefox(firefox_profile=profiles[h])
        browsers[h].set_window_position(0, 0)
        browsers[h].set_window_size(560, 280)
        browsers[h].get('https://www.' + site + '.com/')
        browsers[h].implicitly_wait(5)
        browsers[h].find_element_by_xpath('//*[@id="gh-ac"]').send_keys(search)
        browsers[h].find_element_by_xpath('//*[@id="gh-btn"]').click()        
    	time.sleep(5)

    for m in range(agents):    
        print 'Agent' + str(m+1) + ' started block ' + str(i+1) + ' ' + str(locations[m])
        products = browsers[m].find_elements_by_css_selector('.lvpic.pic.img.left')    
        prices = browsers[m].find_elements_by_xpath("//span[contains(@class,'bold')]")    
        num_results = 0
        
        for price, product in map(None, prices,products):
            if num_results < results:
                product_name = product.get_attribute("iid")
                #print product_name
                price = price.text
                price = re.sub('[^0-9\.]', ' ', price)
                price, sep, tail = price.partition('   ')
                price = re.sub('[^0-9\.]', '', price)
                f.write('%s,%d,%d,%d,%s,%s\n'%(locations[m],i+1,m+1,num_results+1,str(product_name),str(price)))
                num_results = num_results + 1
        print 'Agent' + str(m+1) + ' done block ' + str(i+1) + ' ' + str(locations[m]) 	

    for x in range(agents):
        browsers[x].quit()
    print site + ' ' + country + ' block ' + str(i+1) + ' completed'
f.close()
