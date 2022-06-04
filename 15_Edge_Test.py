from selenium import webdriver
import time

driverPath = "Webdrivers/Edge/Edge_102/msedgedriver.exe"
driver = webdriver.Edge(driverPath)
driver.get("https://www.google.com")
time.sleep(5)
driver.quit()
