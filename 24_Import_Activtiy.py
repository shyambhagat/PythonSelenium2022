import Utilities as util
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # type: ignore
import pandas as pd

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


importProductDF = pd.read_excel('Data/Product_Import.xlsx')

for index, row in importProductDF.iterrows():
    time.sleep(3)
    util.clickButton(browser, By.PARTIAL_LINK_TEXT, 'ADD PRODUCT')
    time.sleep(3)

    util.fillInputBox(browser, By.NAME, "ProductName", row["ProductName"])
    util.fillDropdown(browser, By.NAME, "Supplier", row["Supplier"])
    util.fillDropdown(browser, By.NAME, "Category", row["Category"])
    util.fillInputBox(browser, By.NAME, "QuantityPerUnit", row["QuantityPerUnit"])
    util.fillInputBox(browser, By.NAME, "UnitPrice", row["UnitPrice"])
    util.fillInputBox(browser, By.NAME, "UnitsInStock", row["UnitsInStock"])
    util.fillInputBox(browser, By.NAME, "UnitsOnOrder", row["UnitsOnOrder"])
    util.fillInputBox(browser, By.NAME, "ReorderLevel", row["ReorderLevel"])
    util.fillCheckBox(browser, By.NAME, "Discontinued", row["Discontinued"])
    util.clickButton(browser, By.CSS_SELECTOR, '[value="Save"]')

time.sleep(60)
browser.quit()