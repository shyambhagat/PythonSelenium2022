import imp
import Utilities as util
import time
from selenium.webdriver.common.by import By

driver = util.getChromeDriver()
driver.get("https://www.google.com")
time.sleep(2)

searchInputBox = driver.find_element(By.NAME, "q")
searchInputBox.send_keys("Hello Python")
time.sleep(1)

searchButton = driver.find_element(By.NAME, "btnK")
searchButton.click()
time.sleep(10)

driver.quit()
