from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(options = options)
browser.set_page_load_timeout(30)

browser.get('https://wayscript.com/')

ps = browser.page_source
print(ps)

browser.close()