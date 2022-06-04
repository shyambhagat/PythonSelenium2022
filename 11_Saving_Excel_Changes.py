import Utilities as util
import pandas as pd

def Addition(value1: int, value2: int) -> int:
    return value1 + value2

def Subtraction(value1: int, value2: int) -> int:
    return value1 - value2

def Multiplication(value1: int, value2: int) -> int:
    return value1 * value2

def Division(value1: int, value2: int) -> float:
    return value1 / value2

util.clearScreen
mathTestDF = pd.read_excel("Data/MathDataText.xlsx")

for index, row in mathTestDF.iterrows():
    operation = row["Test Type"]
    param1 = row["Param1"]
    param2 = row["Param2"]
    expectedResult = row["Expected Result"]

    if operation == "Addition":
        result = Addition(param1, param2)
        if result == expectedResult:
            mathTestDF.at[index, "Test Result"] = "Pass"
        else:
            mathTestDF.at[index, "Test Result"] = "Pass"
    elif operation == "Subtraction":
        result = Subtraction(param1, param2)
        mathTestDF.at[index, "Test Result"] = "Pass" if result == expectedResult else "Fail"
    elif operation == "Multiplication":
        result = Multiplication(param1, param2)
        mathTestDF.at[index, "Test Result"] = "Pass" if result == expectedResult else "Fail"
    elif operation == "Division":
        result = Division(param1, param2)
        mathTestDF.at[index, "Test Result"] = "Pass" if result == expectedResult else "Fail"

util.clearScreen()
util.printHeader("Process Start")
print(mathTestDF)
mathTestDF.to_excel("Data/MathDataText.xlsx", index=False)
util.printHeader("Process End")


