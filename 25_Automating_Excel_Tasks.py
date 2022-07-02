import Utilities as util
import pandas as pd

browser = util.getChromeDriver()

automationStepsDF = pd.read_excel("Data/Customer_Automation.xlsx")

for index, row in automationStepsDF.iterrows():
    util.doSeleniumTasks(browser, row)

browser.quit()