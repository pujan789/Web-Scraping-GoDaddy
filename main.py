import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent


chrome_options = webdriver.ChromeOptions()
ua = UserAgent()
user_agent = ua.random
print(user_agent)
chrome_options.add_argument('user-agent={}'.format(user_agent))
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get('https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=bjmtuc.club#')
time.sleep(5)
driver.refresh()
time.sleep(5)
print(driver.find_element(By.CSS_SELECTOR,"[data-cy='pricing-main-price']").text)
driver.quit()