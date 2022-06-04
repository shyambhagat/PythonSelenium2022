from lib2to3.pgen2 import driver
import Utilities as util
import time

#driver = util.getChromeDriver()
#driver = util.getEdgeDriver()
driver = util.getFirefoxDriver()
driver.get("https://www.google.com")
time.sleep(5)
driver.quit()