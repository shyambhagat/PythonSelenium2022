import Utilities as util
import time
from selenium.webdriver.common.by import By

browser = util.getChromeDriver()
browser.get("http://127.0.0.1:8000/admin")
time.sleep(2)

####################### Login #######################
usernameInput = browser.find_element(By.NAME, "username")
usernameInput.send_keys("admin")

passwordInput = browser.find_element(By.NAME, "password")
passwordInput.send_keys("Pass#123")

submitButton = browser.find_element(By.CSS_SELECTOR, '[value="Log in"]')
submitButton.click()
time.sleep(5)

####################### CRUD #######################
regionLink = browser.find_element(By.CSS_SELECTOR, '[href="/admin/Lists/regions/"]')
regionLink.click()
time.sleep(3)

addRegionLink = browser.find_element(By.PARTIAL_LINK_TEXT, 'ADD REGION')
addRegionLink.click()
time.sleep(3)

regionDescInput = browser.find_element(By.NAME, "RegionDescription")
regionDescInput.send_keys("Test Region")

saveButton = browser.find_element(By.CSS_SELECTOR, '[value="Save"]')
saveButton.click()

time.sleep(60)
browser.quit()