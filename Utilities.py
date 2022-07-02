import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.chrome.options import Options as chromeOption
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.edge.options import Options as edgeOption
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.firefox.options import Options as firefoxOption
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # type: ignore


def clearScreen():
    os.system("cls") if os.name == "nt" else os.system("clear")

def printHeader(header):
    print('#' * 80)
    firstHalf = (80 - len(header) - 2) // 2
    print(" " * firstHalf, header)
    print('#' * 80)

def getChromeDriver():
    driverPath = "Webdrivers/Chrome/Chrome_102/chromedriver.exe"
    driverOptions = chromeOption()
    driverOptions.add_argument("--start-maximized")
    driverService = chromeService(executable_path=driverPath)
    return webdriver.Chrome(service=driverService, options=driverOptions)

def getEdgeDriver():
    driverPath = "Webdrivers/Edge/Edge_102/msedgedriver.exe"
    driverOptions = edgeOption()
    driverOptions.add_argument("--start-maximized")
    driverService = edgeService(executable_path=driverPath)
    return webdriver.Edge(service=driverService, options=driverOptions)

def getFirefoxDriver():
    driverPath = "Webdrivers/Firefox/Firefox_101/geckodriver.exe"
    driverOptions = firefoxOption()
    driverOptions.add_argument("--start-maximized")
    driverService = firefoxService(executable_path=driverPath)
    driver = webdriver.Firefox(service=driverService, options=driverOptions)
    driver.maximize_window()
    return driver

def fillInputBox(browser, searchType, filter, inputText):
    inputElement = browser.find_element(searchType, filter)
    inputElement.send_keys(inputText)

def fillDropdown(browser, searchType, filter, inputText):
    inputElement = browser.find_element(searchType, filter)
    inputSelect = Select(inputElement)
    inputSelect.select_by_visible_text(inputText)

def fillCheckBox(browser, searchType, filter, selected):
    inputElement = browser.find_element(searchType, filter)
    if selected and not inputElement.is_selected():    
        inputElement.click()

def clickButton(browser, searchType, filter):
    buttonElement = browser.find_element(searchType, filter)
    buttonElement.click()


def getSelectorType(selectorType):
    if selectorType == "NAME":
        return By.NAME
    elif selectorType == "ID":
        return By.ID
    elif selectorType == "CLASS_NAME":
        return By.CLASS_NAME
    elif selectorType == "CSS_SELECTOR":
        return By.CSS_SELECTOR
    elif selectorType == "LINK_TEXT":
        return By.LINK_TEXT
    elif selectorType == "PARTIAL_LINK_TEXT":
        return By.PARTIAL_LINK_TEXT
    elif selectorType == "TAG_NAME":
        return By.TAG_NAME
    elif selectorType == "XPATH":
        return By.XPATH

def doSeleniumTasks(browser, row):
    action = row["Action"]
    selectorType = row["Selector Type"]
    filter = row["Filter"]
    value = row["Value"]

    if action == "Open Page":
        browser.get(value)
    elif action == "Wait":
        time.sleep(int(value))
    elif action == "Fill Input Box":
        inputSelectorType = getSelectorType(selectorType)
        fillInputBox(browser, inputSelectorType, filter, value)
    elif action == "Fill Drop Down":
        inputSelectorType = getSelectorType(selectorType)
        fillDropdown(browser, inputSelectorType, filter, value)
    elif action == "Fill Check Box":
        inputSelectorType = getSelectorType(selectorType)
        fillCheckBox(browser, inputSelectorType, filter, value)
    elif action == "Button Click":
        inputSelectorType = getSelectorType(selectorType)
        clickButton(browser, inputSelectorType, filter)
