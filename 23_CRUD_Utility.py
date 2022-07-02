import Utilities as util
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # type: ignore

browser = util.getChromeDriver()
browser.get("http://127.0.0.1:8000/admin")
time.sleep(2)

####################### Login #######################
util.fillInputBox(browser, By.NAME, "username", "admin")
util.fillInputBox(browser, By.NAME, "password", "Pass#123")
util.clickButton(browser, By.CSS_SELECTOR, '[value="Log in"]')
time.sleep(5)

####################### CRUD #######################
util.clickButton(browser, By.CSS_SELECTOR, '[href="/admin/Masters/products/"]')
time.sleep(3)

util.clickButton(browser, By.PARTIAL_LINK_TEXT, 'ADD PRODUCT')
time.sleep(3)

util.fillInputBox(browser, By.NAME, "ProductName", "Marie Gold 1Kg")
util.fillDropdown(browser, By.NAME, "Supplier", "Ma Maison")
util.fillDropdown(browser, By.NAME, "Category", "Confections")
util.fillInputBox(browser, By.NAME, "QuantityPerUnit", "1")
util.fillInputBox(browser, By.NAME, "UnitPrice", "8.75")
util.fillInputBox(browser, By.NAME, "UnitsInStock", "10")
util.fillInputBox(browser, By.NAME, "UnitsOnOrder", "60")
util.fillInputBox(browser, By.NAME, "ReorderLevel", "5")
util.fillCheckBox(browser, By.NAME, "Discontinued", True)
util.clickButton(browser, By.CSS_SELECTOR, '[value="Save"]')

time.sleep(60)
browser.quit()