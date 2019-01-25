from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# constants for the app
site_url = 'http://www.szse.cn/disclosure/margin/margin/index.html'
download_path = './stg_rsi_hu'
chromedriver_path = "E:/Utilities/chromedriver.exe"

# set up chrome options
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : download_path}
chromeOptions.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path=chromedriver_path, options=chromeOptions)
driver.implicitly_wait(30)

# Open the website
driver.get(site_url)

print ('site is loading...')

downloadBtns = driver.find_elements_by_xpath("//div[contains(@class, 'report-excel')]//a[contains(@class, 'btn-default-excel')]")
if len(downloadBtns) > 0:
    downloadBtns[0].send_keys("\n")

driver.implicitly_wait(100)
# driver.quit()



