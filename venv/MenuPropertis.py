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
    userInput = input()
    if(userInput == "<"):
        return lambda a: a < GetDigitUserInput()
    elif(userInput == "<="):
        return lambda a: a <= GetDigitUserInput()
    elif(userInput == "=="):
        return lambda a: a == GetDigitUserInput()
    elif(userInput == ">="):
        return lambda a: a >= GetDigitUserInput()
    elif(userInput == ">"):
        return lambda a: a > GetDigitUserInput()
    elif(userInput == "!="):
        return lambda a: a != GetDigitUserInput()

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
    for i in FilterValue(base, filter):
        print(i)