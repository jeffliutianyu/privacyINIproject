from selenium import webdriver as wd
import sys, re, time, argparse
reload(sys)
sys.setdefaultencoding('utf-8')

# NOTE: For ebay, we take the product id instead of product name due to repeated product name

site = 'ebay'
search = 'back support'
num_block = 10
results = 30

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

#open files
f1 = open(site + '_' + country + '.txt', 'wb')

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

    browser1.get('https://www.' + site + '.com/')
    browser1.implicitly_wait(5)
    browser1.find_element_by_xpath('//*[@id="gh-ac"]').send_keys(search)
    browser1.find_element_by_xpath('//*[@id="gh-btn"]').click()

    browser2.get('https://www.' + site + '.com/')
    browser2.implicitly_wait(5)
    browser2.find_element_by_xpath('//*[@id="gh-ac"]').send_keys(search)
    browser2.find_element_by_xpath('//*[@id="gh-btn"]').click()

    browser3.get('https://www.' + site + '.com/')
    browser3.implicitly_wait(5)
    browser3.find_element_by_xpath('//*[@id="gh-ac"]').send_keys(search)
    browser3.find_element_by_xpath('//*[@id="gh-btn"]').click()    

    browser4.get('https://www.' + site + '.com/')
    browser4.implicitly_wait(5)
    browser4.find_element_by_xpath('//*[@id="gh-ac"]').send_keys(search)
    browser4.find_element_by_xpath('//*[@id="gh-btn"]').click()
        
    time.sleep(2)
    #print 'browser 1: ' + str(browser1.current_url)
    print 'Agent 1 start '+ 'block ' + str(i+1) + ' ' + location1
    
    products = browser1.find_elements_by_css_selector('.lvpic.pic.img.left')    
    prices = browser1.find_elements_by_xpath("//span[contains(@class,'bold')]")    
    num_results = 0
    
    for price, product in map(None, prices,products):
        if num_results < results:
            product_name = product.get_attribute("iid")
            #print product_name
            price = price.text
            price = re.sub('[^0-9\.]', ' ', price)
            price, sep, tail = price.partition('   ')
            price = re.sub('[^0-9\.]', '', price)
            f1.write('%s,%d,%d,%d,%s,%s\n'%(location1,i+1,1,num_results+1,str(product_name),str(price)))
            num_results = num_results + 1
    time.sleep(2) 
    print 'Agent 1 done '+ 'block ' + str(i+1) + ' ' + location1	

    print 'Agent 2 start '+ 'block ' + str(i+1) + ' ' + location1
    #print 'browser 2: ' + str(browser2.current_url)
        
    products = browser2.find_elements_by_css_selector('.lvpic.pic.img.left')    
    prices = browser2.find_elements_by_xpath("//span[contains(@class,'bold')]")    
    num_results = 0
    
    for price, product in map(None, prices,products):
        if num_results < results:
            product_name = product.get_attribute("iid")
            price = price.text
            price = re.sub('[^0-9\.]', ' ', price)
            price, sep, tail = price.partition('   ')
            price = re.sub('[^0-9\.]', '', price)
            f1.write('%s,%d,%d,%d,%s,%s\n'%(location1,i+1,2,num_results+1,str(product_name),str(price)))
            num_results = num_results + 1
    time.sleep(2) 
    print 'Agent 2 done '+ 'block ' + str(i+1) + ' ' + location1

    print 'Agent 3 start '+ 'block ' + str(i+1) + ' ' + location2
    #print 'browser 3: ' + str(browser3.current_url)
        
    products = browser3.find_elements_by_css_selector('.lvpic.pic.img.left')    
    prices = browser3.find_elements_by_xpath("//span[contains(@class,'bold')]")    
    num_results = 0
    
    for price, product in map(None, prices,products):
        if num_results < results:
            product_name = product.get_attribute("iid")
            price = price.text
            price = re.sub('[^0-9\.]', ' ', price)
            price, sep, tail = price.partition('   ')
            price = re.sub('[^0-9\.]', '', price)
            f1.write('%s,%d,%d,%d,%s,%s\n'%(location2,i+1,3,num_results+1,str(product_name),str(price)))
            num_results = num_results + 1
    print 'Agent 3 done '+ 'block ' + str(i+1) + ' ' + location2

    print 'Agent 4 start '+ 'block ' + str(i+1) + ' ' + location2
    #print 'browser 4: ' + str(browser4.current_url)
        
    products = browser4.find_elements_by_css_selector('.lvpic.pic.img.left')    
    prices = browser4.find_elements_by_xpath("//span[contains(@class,'bold')]")    
    num_results = 0
    
    for price, product in map(None, prices,products):
        if num_results < results:
            product_name = product.get_attribute("iid")
            price = price.text
            price = re.sub('[^0-9\.]', ' ', price)
            price, sep, tail = price.partition('   ')
            price = re.sub('[^0-9\.]', '', price)
            f1.write('%s,%d,%d,%d,%s,%s\n'%(location2,i+1,4,num_results+1,str(product_name),str(price)))
            num_results = num_results + 1
    time.sleep(2)
    print 'Agent 4 done '+ 'block ' + str(i+1) + ' ' + location2	
    browser1.quit()
    browser2.quit()
    browser3.quit()
    browser4.quit()
    print site + ' ' + country + ' block ' + str(i+1) + ' completed'    

f1.close()
