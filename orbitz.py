from selenium import webdriver as wd
import sys, time, re, argparse
reload(sys)
sys.setdefaultencoding('utf-8')

results = 30
num_block = 10

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
    location1 = 'LA'
    location2 = 'AH'
    country = 'usa'
elif args.taiwan:
    location1 = 'taipei'
    location2 = 'hsinchu'
    country = 'taiwan'
elif args.indonesia:
    location1 = 'jakarta'
    location2 = 'makasser'
    country = 'indonesia'
elif args.germany:
    location1 = 'baden'
    location2 = 'kiez'
    country = 'germany'
elif args.china:
    location1 = 'beijing'
    location2 = 'nanning'
    country = 'china'
elif args.china:
    location1 = 'parana'
    location2 = 'osasco'
    country = 'brazil'
elif args.usa_vs_indo:
    location1 = 'usa'
    location2 = 'indonesia'
    country = 'usa_vs_indonesia'
else:
    parser.print_help()
    sys.exit(1)	

f1 = open(site + '_' + country + '.txt','wb')

for i in range(num_block):

    print site + ' ' + country + ' block ' + str(i+1) + ' started'
    
    if args.usa:     
        #set firefox profiles
        profile1 = wd.FirefoxProfile()
        profile1.set_preference("network.proxy.type", 1)
        profile1.set_preference("network.proxy.https", "174.138.54.111")
        profile1.set_preference("network.proxy.https_port", "3218")
        profile1.set_preference("dom.disable_beforeunload", True)
        profile1.set_preference("dom.popup_maximum", 0)
        profile1.set_preference("privacy.popups.showBrowserMessage", False)
        profile1.set_preference("browser.cache.disk.enable", False)
        profile1.set_preference("browser.cache.memory.enable", False)
        profile1.set_preference("browser.cache.offline.enable", False)
        profile1.set_preference("network.http.use-cache", False)
        profile1.update_preferences()

        profile2 = wd.FirefoxProfile()
        profile2.set_preference("network.proxy.type", 1)
        profile2.set_preference("network.proxy.https", "174.138.54.111")
        profile2.set_preference("network.proxy.https_port", "3218")
        profile2.set_preference("dom.disable_beforeunload", True)
        profile2.set_preference("dom.popup_maximum", 0)
        profile2.set_preference("privacy.popups.showBrowserMessage", False)
        profile2.set_preference("browser.cache.disk.enable", False)
        profile2.set_preference("browser.cache.memory.enable", False)
        profile2.set_preference("browser.cache.offline.enable", False)
        profile2.set_preference("network.http.use-cache", False)
        profile2.update_preferences()
        
        profile3 = wd.FirefoxProfile()
        profile3.set_preference("network.proxy.type", 1)
        profile3.set_preference("network.proxy.https", "35.201.253.111")
        profile3.set_preference("network.proxy.https_port", "3218")
        profile3.set_preference("dom.disable_beforeunload", True)
        profile3.set_preference("dom.popup_maximum", 0)
        profile3.set_preference("privacy.popups.showBrowserMessage", False)
        profile3.set_preference("browser.cache.disk.enable", False)
        profile3.set_preference("browser.cache.memory.enable", False)
        profile3.set_preference("browser.cache.offline.enable", False)
        profile3.set_preference("network.http.use-cache", False)
        profile3.update_preferences()

        profile4 = wd.FirefoxProfile()
        profile4.set_preference("network.proxy.type", 1)
        profile4.set_preference("network.proxy.https", "35.201.253.111")
        profile4.set_preference("network.proxy.https_port", "3218")
        profile4.set_preference("dom.disable_beforeunload", True)
        profile4.set_preference("dom.popup_maximum", 0)
        profile4.set_preference("privacy.popups.showBrowserMessage", False)
        profile4.set_preference("browser.cache.disk.enable", False)
        profile4.set_preference("browser.cache.memory.enable", False)
        profile4.set_preference("browser.cache.offline.enable", False)
        profile4.set_preference("network.http.use-cache", False)
        profile4.update_preferences()

    elif args.taiwan:
        #set firefox profiles
        profile1 = wd.FirefoxProfile()
        profile1.set_preference("network.proxy.type", 1)
        profile1.set_preference("network.proxy.https", "61.216.24.97")
        profile1.set_preference("network.proxy.https_port", "3128")
        profile1.set_preference("dom.disable_beforeunload", True)
        profile1.set_preference("dom.popup_maximum", 0)
        profile1.set_preference("privacy.popups.showBrowserMessage", False)
        profile1.set_preference("browser.cache.disk.enable", False)
        profile1.set_preference("browser.cache.memory.enable", False)
        profile1.set_preference("browser.cache.offline.enable", False)
        profile1.set_preference("network.http.use-cache", False)
        profile1.update_preferences()

        profile2 = wd.FirefoxProfile()
        profile2.set_preference("network.proxy.type", 1)
        profile2.set_preference("network.proxy.https", "61.216.24.97")
        profile2.set_preference("network.proxy.https_port", "3128")
        profile2.set_preference("dom.disable_beforeunload", True)
        profile2.set_preference("dom.popup_maximum", 0)
        profile2.set_preference("privacy.popups.showBrowserMessage", False)
        profile2.set_preference("browser.cache.disk.enable", False)
        profile2.set_preference("browser.cache.memory.enable", False)
        profile2.set_preference("browser.cache.offline.enable", False)
        profile2.set_preference("network.http.use-cache", False)
        profile2.update_preferences()

        profile3 = wd.FirefoxProfile()
        profile3.set_preference("network.proxy.type", 1)
        profile3.set_preference("network.proxy.https", "211.79.61.8")
        profile3.set_preference("network.proxy.https_port", "3128")
        profile3.set_preference("dom.disable_beforeunload", True)
        profile3.set_preference("dom.popup_maximum", 0)
        profile3.set_preference("privacy.popups.showBrowserMessage", False)
        profile3.set_preference("browser.cache.disk.enable", False)
        profile3.set_preference("browser.cache.memory.enable", False)
        profile3.set_preference("browser.cache.offline.enable", False)
        profile3.set_preference("network.http.use-cache", False)
        profile3.update_preferences()

        profile4 = wd.FirefoxProfile()
        profile4.set_preference("network.proxy.type", 1)
        profile4.set_preference("network.proxy.https", "211.79.61.8")
        profile4.set_preference("network.proxy.https_port", "3128")
        profile4.set_preference("dom.disable_beforeunload", True)
        profile4.set_preference("dom.popup_maximum", 0)
        profile4.set_preference("privacy.popups.showBrowserMessage", False)
        profile4.set_preference("browser.cache.disk.enable", False)
        profile4.set_preference("browser.cache.memory.enable", False)
        profile4.set_preference("browser.cache.offline.enable", False)
        profile4.set_preference("network.http.use-cache", False)
        profile4.update_preferences()

    elif args.indonesia:
        #set firefox profiles
        profile1 = wd.FirefoxProfile()
        profile1.set_preference("network.proxy.type", 1)
        profile1.set_preference("network.proxy.https", "36.67.108.53")
        profile1.set_preference("network.proxy.https_port", "62225")
        profile1.set_preference("dom.disable_beforeunload", True)
        profile1.set_preference("dom.popup_maximum", 0)
        profile1.set_preference("privacy.popups.showBrowserMessage", False)
        profile1.set_preference("browser.cache.disk.enable", False)
        profile1.set_preference("browser.cache.memory.enable", False)
        profile1.set_preference("browser.cache.offline.enable", False)
        profile1.set_preference("network.http.use-cache", False)
        profile1.update_preferences()

        profile2 = wd.FirefoxProfile()
        profile2.set_preference("network.proxy.type", 1)
        profile2.set_preference("network.proxy.https", "36.67.108.53")
        profile2.set_preference("network.proxy.https_port", "62225")
        profile2.set_preference("dom.disable_beforeunload", True)
        profile2.set_preference("dom.popup_maximum", 0)
        profile2.set_preference("privacy.popups.showBrowserMessage", False)
        profile2.set_preference("browser.cache.disk.enable", False)
        profile2.set_preference("browser.cache.memory.enable", False)
        profile2.set_preference("browser.cache.offline.enable", False)
        profile2.set_preference("network.http.use-cache", False)
        profile2.update_preferences()

        profile3 = wd.FirefoxProfile()
        profile3.set_preference("network.proxy.type", 1)
        profile3.set_preference("network.proxy.https", "202.124.205.26")
        profile3.set_preference("network.proxy.https_port", "3128")
        profile3.set_preference("dom.disable_beforeunload", True)
        profile3.set_preference("dom.popup_maximum", 0)
        profile3.set_preference("privacy.popups.showBrowserMessage", False)
        profile3.set_preference("browser.cache.disk.enable", False)
        profile3.set_preference("browser.cache.memory.enable", False)
        profile3.set_preference("browser.cache.offline.enable", False)
        profile3.set_preference("network.http.use-cache", False)
        profile3.update_preferences()

        profile4 = wd.FirefoxProfile()
        profile4.set_preference("network.proxy.type", 1)
        profile4.set_preference("network.proxy.https", "202.124.205.26")
        profile4.set_preference("network.proxy.https_port", "3128")
        profile4.set_preference("dom.disable_beforeunload", True)
        profile4.set_preference("dom.popup_maximum", 0)
        profile4.set_preference("privacy.popups.showBrowserMessage", False)
        profile4.set_preference("browser.cache.disk.enable", False)
        profile4.set_preference("browser.cache.memory.enable", False)
        profile4.set_preference("browser.cache.offline.enable", False)
        profile4.set_preference("network.http.use-cache", False)
        profile4.update_preferences()

    elif args.germany:
        #set firefox profiles
        profile1 = wd.FirefoxProfile()
        profile1.set_preference("network.proxy.type", 1)
        profile1.set_preference("network.proxy.https", "149.172.246.81")
        profile1.set_preference("network.proxy.https_port", "3218")
        profile1.set_preference("dom.disable_beforeunload", True)
        profile1.set_preference("dom.popup_maximum", 0)
        profile1.set_preference("privacy.popups.showBrowserMessage", False)
        profile1.set_preference("browser.cache.disk.enable", False)
        profile1.set_preference("browser.cache.memory.enable", False)
        profile1.set_preference("browser.cache.offline.enable", False)
        profile1.set_preference("network.http.use-cache", False)
        profile1.update_preferences()

        profile2 = wd.FirefoxProfile()
        profile2.set_preference("network.proxy.type", 1)
        profile2.set_preference("network.proxy.https", "149.172.246.81")
        profile2.set_preference("network.proxy.https_port", "3218")
        profile2.set_preference("dom.disable_beforeunload", True)
        profile2.set_preference("dom.popup_maximum", 0)
        profile2.set_preference("privacy.popups.showBrowserMessage", False)
        profile2.set_preference("browser.cache.disk.enable", False)
        profile2.set_preference("browser.cache.memory.enable", False)
        profile2.set_preference("browser.cache.offline.enable", False)
        profile2.set_preference("network.http.use-cache", False)
        profile2.update_preferences()

        profile3 = wd.FirefoxProfile()
        profile3.set_preference("network.proxy.type", 1)
        profile3.set_preference("network.proxy.https", "138.201.51.141")
        profile3.set_preference("network.proxy.https_port", "3218")
        profile3.set_preference("dom.disable_beforeunload", True)
        profile3.set_preference("dom.popup_maximum", 0)
        profile3.set_preference("privacy.popups.showBrowserMessage", False)
        profile3.set_preference("browser.cache.disk.enable", False)
        profile3.set_preference("browser.cache.memory.enable", False)
        profile3.set_preference("browser.cache.offline.enable", False)
        profile3.set_preference("network.http.use-cache", False)
        profile3.update_preferences()

        profile4 = wd.FirefoxProfile()
        profile4.set_preference("network.proxy.type", 1)
        profile4.set_preference("network.proxy.https", "138.201.51.141")
        profile4.set_preference("network.proxy.https_port", "3218")
        profile4.set_preference("dom.disable_beforeunload", True)
        profile4.set_preference("dom.popup_maximum", 0)
        profile4.set_preference("privacy.popups.showBrowserMessage", False)
        profile4.set_preference("browser.cache.disk.enable", False)
        profile4.set_preference("browser.cache.memory.enable", False)
        profile4.set_preference("browser.cache.offline.enable", False)
        profile4.set_preference("network.http.use-cache", False)
        profile4.update_preferences()

    elif args.china:    
        #set firefox profiles
        profile1 = wd.FirefoxProfile()
        profile1.set_preference("network.proxy.type", 1)
        profile1.set_preference("network.proxy.https", "61.160.208.222")
        profile1.set_preference("network.proxy.https_port", "8080")
        profile1.set_preference("dom.disable_beforeunload", True)
        profile1.set_preference("dom.popup_maximum", 0)
        profile1.set_preference("privacy.popups.showBrowserMessage", False)
        profile1.set_preference("browser.cache.disk.enable", False)
        profile1.set_preference("browser.cache.memory.enable", False)
        profile1.set_preference("browser.cache.offline.enable", False)
        profile1.set_preference("network.http.use-cache", False)
        profile1.update_preferences()

        profile2 = wd.FirefoxProfile()
        profile2.set_preference("network.proxy.type", 1)
        profile2.set_preference("network.proxy.https", "61.160.208.222")
        profile2.set_preference("network.proxy.https_port", "8080")
        profile2.set_preference("dom.disable_beforeunload", True)
        profile2.set_preference("dom.popup_maximum", 0)
        profile2.set_preference("privacy.popups.showBrowserMessage", False)
        profile2.set_preference("browser.cache.disk.enable", False)
        profile2.set_preference("browser.cache.memory.enable", False)
        profile2.set_preference("browser.cache.offline.enable", False)
        profile2.set_preference("network.http.use-cache", False)
        profile2.update_preferences()

        profile3 = wd.FirefoxProfile()
        profile3.set_preference("network.proxy.type", 1)
        profile3.set_preference("network.proxy.https", "116.11.254.37")
        profile3.set_preference("network.proxy.https_port", "80")
        profile3.set_preference("dom.disable_beforeunload", True)
        profile3.set_preference("dom.popup_maximum", 0)
        profile3.set_preference("privacy.popups.showBrowserMessage", False)
        profile3.set_preference("browser.cache.disk.enable", False)
        profile3.set_preference("browser.cache.memory.enable", False)
        profile3.set_preference("browser.cache.offline.enable", False)
        profile3.set_preference("network.http.use-cache", False)
        profile3.update_preferences()

        profile4 = wd.FirefoxProfile()
        profile4.set_preference("network.proxy.type", 1)
        profile4.set_preference("network.proxy.https", "116.11.254.37")
        profile4.set_preference("network.proxy.https_port", "80")
        profile4.set_preference("dom.disable_beforeunload", True)
        profile4.set_preference("dom.popup_maximum", 0)
        profile4.set_preference("privacy.popups.showBrowserMessage", False)
        profile4.set_preference("browser.cache.disk.enable", False)
        profile4.set_preference("browser.cache.memory.enable", False)
        profile4.set_preference("browser.cache.offline.enable", False)
        profile4.set_preference("network.http.use-cache", False)
        profile4.update_preferences()

    elif args.brazil:
        #set firefox profiles
        profile1 = wd.FirefoxProfile()
        profile1.set_preference("network.proxy.type", 1)
        profile1.set_preference("network.proxy.https", "189.115.92.71")
        profile1.set_preference("network.proxy.https_port", "80")
        profile1.set_preference("dom.disable_beforeunload", True)
        profile1.set_preference("dom.popup_maximum", 0)
        profile1.set_preference("privacy.popups.showBrowserMessage", False)
        profile1.set_preference("browser.cache.disk.enable", False)
        profile1.set_preference("browser.cache.memory.enable", False)
        profile1.set_preference("browser.cache.offline.enable", False)
        profile1.set_preference("network.http.use-cache", False)
        profile1.update_preferences()

        profile2 = wd.FirefoxProfile()
        profile2.set_preference("network.proxy.type", 1)
        profile2.set_preference("network.proxy.https", "189.115.92.71")
        profile2.set_preference("network.proxy.https_port", "80")
        profile2.set_preference("dom.disable_beforeunload", True)
        profile2.set_preference("dom.popup_maximum", 0)
        profile2.set_preference("privacy.popups.showBrowserMessage", False)
        profile2.set_preference("browser.cache.disk.enable", False)
        profile2.set_preference("browser.cache.memory.enable", False)
        profile2.set_preference("browser.cache.offline.enable", False)
        profile2.set_preference("network.http.use-cache", False)
        profile2.update_preferences()

        profile3 = wd.FirefoxProfile()
        profile3.set_preference("network.proxy.type", 1)
        profile3.set_preference("network.proxy.https", "177.8.169.254")
        profile3.set_preference("network.proxy.https_port", "3128")
        profile3.set_preference("dom.disable_beforeunload", True)
        profile3.set_preference("dom.popup_maximum", 0)
        profile3.set_preference("privacy.popups.showBrowserMessage", False)
        profile3.set_preference("browser.cache.disk.enable", False)
        profile3.set_preference("browser.cache.memory.enable", False)
        profile3.set_preference("browser.cache.offline.enable", False)
        profile3.set_preference("network.http.use-cache", False)
        profile3.update_preferences()

        profile4 = wd.FirefoxProfile()
        profile4.set_preference("network.proxy.type", 1)
        profile4.set_preference("network.proxy.https", "177.8.169.254")
        profile4.set_preference("network.proxy.https_port", "3128")
        profile4.set_preference("dom.disable_beforeunload", True)
        profile4.set_preference("dom.popup_maximum", 0)
        profile4.set_preference("privacy.popups.showBrowserMessage", False)
        profile4.set_preference("browser.cache.disk.enable", False)
        profile4.set_preference("browser.cache.memory.enable", False)
        profile4.set_preference("browser.cache.offline.enable", False)
        profile4.set_preference("network.http.use-cache", False)
        profile4.update_preferences()

    elif args.usa_vs_indo:
        #set firefox profiles
        profile1 = wd.FirefoxProfile()
        profile1.set_preference("network.proxy.type", 1)
        profile1.set_preference("network.proxy.https", "174.138.54.111")
        profile1.set_preference("network.proxy.https_port", "3218")
        profile1.set_preference("dom.disable_beforeunload", True)
        profile1.set_preference("dom.popup_maximum", 0)
        profile1.set_preference("privacy.popups.showBrowserMessage", False)
        profile1.set_preference("browser.cache.disk.enable", False)
        profile1.set_preference("browser.cache.memory.enable", False)
        profile1.set_preference("browser.cache.offline.enable", False)
        profile1.set_preference("network.http.use-cache", False)
        profile1.update_preferences()
        
        profile2 = wd.FirefoxProfile()
        profile2.set_preference("network.proxy.type", 1)
        profile2.set_preference("network.proxy.https", "174.138.54.111")
        profile2.set_preference("network.proxy.https_port", "3218")
        profile2.set_preference("dom.disable_beforeunload", True)
        profile2.set_preference("dom.popup_maximum", 0)
        profile2.set_preference("privacy.popups.showBrowserMessage", False)
        profile2.set_preference("browser.cache.disk.enable", False)
        profile2.set_preference("browser.cache.memory.enable", False)
        profile2.set_preference("browser.cache.offline.enable", False)
        profile2.set_preference("network.http.use-cache", False)
        profile2.update_preferences()

        profile3 = wd.FirefoxProfile()
        profile3.set_preference("network.proxy.type", 1)
        profile3.set_preference("network.proxy.https", "202.124.205.26")
        profile3.set_preference("network.proxy.https_port", "3128")
        profile3.set_preference("dom.disable_beforeunload", True)
        profile3.set_preference("dom.popup_maximum", 0)
        profile3.set_preference("privacy.popups.showBrowserMessage", False)
        profile3.set_preference("browser.cache.disk.enable", False)
        profile3.set_preference("browser.cache.memory.enable", False)
        profile3.set_preference("browser.cache.offline.enable", False)
        profile3.set_preference("network.http.use-cache", False)
        profile3.update_preferences()

        profile4 = wd.FirefoxProfile()
        profile4.set_preference("network.proxy.type", 1)
        profile4.set_preference("network.proxy.https", "202.124.205.26")
        profile4.set_preference("network.proxy.https_port", "3128")
        profile4.set_preference("dom.disable_beforeunload", True)
        profile4.set_preference("dom.popup_maximum", 0)
        profile4.set_preference("privacy.popups.showBrowserMessage", False)
        profile4.set_preference("browser.cache.disk.enable", False)
        profile4.set_preference("browser.cache.memory.enable", False)
        profile4.set_preference("browser.cache.offline.enable", False)
        profile4.set_preference("network.http.use-cache", False)
        profile4.update_preferences()
        
    #set browser profiles
    browser1 = wd.Firefox(firefox_profile=profile1)
    browser1.set_window_position(0, 0)
    browser1.set_window_size(560, 280)
    
    browser2 = wd.Firefox(firefox_profile=profile2)
    browser2.set_window_position(0, 2)
    browser2.set_window_size(560, 280)
    
    browser3 = wd.Firefox(firefox_profile=profile3)
    browser3.set_window_position(2, 0)
    browser3.set_window_size(560, 280)
    
    browser4 = wd.Firefox(firefox_profile=profile4)
    browser4.set_window_position(2, 2)
    browser4.set_window_size(560, 280)
    
    # 1st agent location1
    browser1.get('https://www.orbitz.com/Hotel-Search?#&destination=Singapore%20(all)%2C%20Singapore&startDate=12/12/2017&endDate=12/30/2017&regionId=180027&latLong=1.290270,103.852010&adults=2') #go to site

    default = browser1.window_handles[0] #get the handle number for default window`
    #print 'browser handle is: ' + str(default)

    browser1.switch_to.window(default)
    #print 'current url is: ' + str(browser1.current_url)
    
    time.sleep(5)
    num_results = 0
    print 'Agent 1 started '+ 'block ' + str(i+1) + ' ' + location1

    prices = browser1.find_elements_by_xpath('//article[@id]')
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
                #new_price,sep,tail = new_price.partition('\n')
            
            new_price = re.sub('[^0-9\.]', '', new_price)
            num_results = num_results+1    
            f1.write('%s,%d,%d,%d,%s,%s\n'%(location1,i+1,1,num_results,new_product,new_price))    
    print 'Agent 1 done '+ 'block ' + str(i+1) + ' ' + location1

    # 1st agent location1
    browser2.get('https://www.orbitz.com/Hotel-Search?#&destination=Singapore%20(all)%2C%20Singapore&startDate=12/12/2017&endDate=12/30/2017&regionId=180027&latLong=1.290270,103.852010&adults=2') #go to site

    default = browser2.window_handles[0] #get the handle number for default window`
    #print 'browser handle is: ' + str(default)

    browser2.switch_to.window(default)
    #print 'current url is: ' + str(browser2.current_url)
    
    time.sleep(5)
    num_results = 0
    print 'Agent 2 started '+ 'block ' + str(i+1) + ' ' + location1

    prices = browser2.find_elements_by_xpath('//article[@id]')
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
                #new_price,sep,tail = new_price.partition('\n')
            
            new_price = re.sub('[^0-9\.]', '', new_price)
            num_results = num_results+1
            f1.write('%s,%d,%d,%d,%s,%s\n'%(location1,i+1,2,num_results,new_product,new_price)) 

    print 'Agent 2 done '+ 'block ' + str(i+1) + ' ' + location1

    # 2nd agent location1
    browser3.get('https://www.orbitz.com/Hotel-Search?#&destination=Singapore%20(all)%2C%20Singapore&startDate=12/12/2017&endDate=12/30/2017&regionId=180027&latLong=1.290270,103.852010&adults=2') #go to site

    default = browser3.window_handles[0] #get the handle number for default window`
    #print 'browser handle is: ' + str(default)

    browser3.switch_to.window(default)
    #print 'current url is: ' + str(browser3.current_url)
    
    time.sleep(5)
    num_results = 0
    print 'Agent 3 started '+ 'block ' + str(i+1) + ' ' + location2

    prices = browser3.find_elements_by_xpath('//article[@id]')
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
                #new_price,sep,tail = new_price.partition('\n')
            
            new_price = re.sub('[^0-9\.]', '', new_price)
            num_results = num_results+1
            f1.write('%s,%d,%d,%d,%s,%s\n'%(location2,i+1,3,num_results,new_product,new_price))       
    print 'Agent 3 done '+ 'block ' + str(i+1) + ' ' + location2

    # 2nd agent location1
    browser4.get('https://www.orbitz.com/Hotel-Search?#&destination=Singapore%20(all)%2C%20Singapore&startDate=12/12/2017&endDate=12/30/2017&regionId=180027&latLong=1.290270,103.852010&adults=2') #go to site

    default = browser4.window_handles[0] #get the handle number for default window`
    #print 'browser handle is: ' + str(default)

    browser4.switch_to.window(default)
    #print 'current url is: ' + str(browser4.current_url)
    
    time.sleep(5)
    num_results = 0
    print 'Agent 4 started '+ 'block ' + str(i+1) + ' ' + location2

    prices = browser4.find_elements_by_xpath('//article[@id]')
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
                #new_price,sep,tail = new_price.partition('\n')
            
            new_price = re.sub('[^0-9\.]', '', new_price)
            num_results = num_results+1
            f1.write('%s,%d,%d,%d,%s,%s\n'%(location2,i+1,4,num_results,new_product,new_price)) 
	
    print 'Agent 4 done '+ 'block ' + str(i+1) + ' ' + location2
    browser1.quit()
    browser2.quit()
    browser3.quit()
    browser4.quit()
    print site + ' ' + country + ' block ' + str(i+1) + ' completed'
f1.close()








