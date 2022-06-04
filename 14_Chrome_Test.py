from selenium import webdriver
import time

driverPath = "Webdrivers/Chrome/Chrome_102/chromedriver.exe"
driver = webdriver.Chrome(driverPath)
driver.get("https://www.google.com")
time.sleep(5)
driver.quit()
