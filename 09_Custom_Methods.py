import os

def clearScreen():
    # if os.name == "nt":
    #     os.system("cls")
    # else:
    #     os.system("clear")
    os.system("cls") if os.name == "nt" else os.system("clear")

def printHeader(header):
    print('#' * 80)
    firstHalf = (80 - len(header) - 2) // 2
    print(" " * firstHalf, header)
    print('#' * 80)


clearScreen()
printHeader("Process Start")
print("Test")
printHeader("Process End")