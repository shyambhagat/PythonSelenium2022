from selenium import webdriver
import time

driverPath = "Webdrivers/Firefox/Firefox_101/geckodriver.exe"
driver = webdriver.Firefox(executable_path=driverPath)
driver.get("https://www.google.com")
time.sleep(5)
driver.quit()
