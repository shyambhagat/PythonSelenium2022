import Utilities as util
import time
from selenium.webdriver.common.by import By

browser = util.getChromeDriver()
browser.get("http://127.0.0.1:8000/admin")
time.sleep(2)

usernameInput = browser.find_element(By.NAME, "username")
usernameInput.send_keys("admin")

passwordInput = browser.find_element(By.NAME, "password")
passwordInput.send_keys("Pass#123")

submitButton = browser.find_element(By.CSS_SELECTOR, '[value="Log in"]')
submitButton.click()
time.sleep(10)

logoutButton = browser.find_element(By.CSS_SELECTOR, '[href="/admin/logout/"]')
logoutButton.click()

time.sleep(60)
browser.quit()