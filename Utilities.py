import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.chrome.options import Options as chromeOption
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.edge.options import Options as edgeOption
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.firefox.options import Options as firefoxOption


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
