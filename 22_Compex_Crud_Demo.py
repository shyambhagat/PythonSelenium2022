import Utilities as util
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # type: ignore

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
productLink = browser.find_element(By.CSS_SELECTOR, '[href="/admin/Masters/products/"]')
productLink.click()
time.sleep(3)

addProdcutLink = browser.find_element(By.PARTIAL_LINK_TEXT, 'ADD PRODUCT')
addProdcutLink.click()
time.sleep(3)

regionDescInput = browser.find_element(By.NAME, "ProductName")
regionDescInput.send_keys("Marie Gold")

supplierInput = browser.find_element(By.NAME, "Supplier")
supplierSelect = Select(supplierInput)
supplierSelect.select_by_visible_text("Ma Maison")

categoryInput = browser.find_element(By.NAME, "Category")
categorySelect = Select(categoryInput)
categorySelect.select_by_visible_text("Confections")

quantityPerUnitInput = browser.find_element(By.NAME, "QuantityPerUnit")
quantityPerUnitInput.send_keys("1")

unitPriceInput = browser.find_element(By.NAME, "UnitPrice")
unitPriceInput.send_keys("8.75")

unitsInStockInput = browser.find_element(By.NAME, "UnitsInStock")
unitsInStockInput.send_keys("10")

unitsOnOrderInput = browser.find_element(By.NAME, "UnitsOnOrder")
unitsOnOrderInput.send_keys("60")

reorderLevelInput = browser.find_element(By.NAME, "ReorderLevel")
reorderLevelInput.send_keys(1)

discontinuedInput = browser.find_element(By.NAME, "Discontinued")
discontinuedInput.click()

saveButton = browser.find_element(By.CSS_SELECTOR, '[value="Save"]')
saveButton.click()

time.sleep(60)
browser.quit()