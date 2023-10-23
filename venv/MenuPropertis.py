from UI import *
from  DateBaseTools import *
import AdminsData as DB


def GetMainMenu() -> IElement:
    getMin = Button("MinValue", lambda: print(GetMinValue(DB.SystemAdminsPayments)))
    getMax = Button("MaxValue", lambda: print(GetMaxValue(DB.SystemAdminsPayments)))
    getAverage = Button("Average", lambda: print(GetAverage(DB.SystemAdminsPayments)))

    getFilterValue = Button("Filter", lambda: PrintFilterValue(DB.SystemAdminsPayments, GetFilterValueSetingsMenu()))


    dataBaseMenuOptions = ItemContainer("Options")
    dataBaseMenuOptions.AddChildren(getMax)
    dataBaseMenuOptions.AddChildren(getMin)
    dataBaseMenuOptions.AddChildren(getAverage)

    dataBaseMenuOtherOptions = ItemContainer("Other options")
    dataBaseMenuOtherOptions.AddChildren(getFilterValue)

    appLication = ItemContainer("Main")

    appLication.AddChildren(dataBaseMenuOptions)
    appLication.AddChildren(dataBaseMenuOtherOptions)

    return  appLication


def GetFilterValueSetingsMenu():
    print("Chose operation")
    print("<\n<=\n==\n>=\n>\n!=")
    operation = input()
    number = GetDigitUserInput()
    if(operation == "<"):
        return lambda a: a < number
    elif(operation == "<="):
        return lambda a: a <= number
    elif(operation == "=="):
        return lambda a: a == number
    elif(operation == ">="):
        return lambda a: a >= number
    elif(operation == ">"):
        return lambda a: a > number
    elif(operation == "!="):
        return lambda a: a != number

def GetDigitUserInput():
    print("Write value")
    while True:
        try:
            userInput = int(input('->'))
        except:
            print("Тут")
            continue
        break
    return userInput


def PrintFilterValue(base: dict, filter):
    m = FilterValue(base, filter)
    for i in m:
        print(i)