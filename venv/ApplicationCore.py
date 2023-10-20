import MenuPropertis
from UI import Item, ItemContainer, Button

class Application:

    def __init__(self, base: dict):
        self.__base = base
        self.__historyMenu = [MenuPropertis.GetMainMenu()]


    def RunApplication(self):
        loop = True
        while(loop):
            print("*" * 20)
            self.__historyMenu[-1].DisplayChildrens()
            userInput = input()

            if(userInput == self.__historyMenu[0].Name()):
                loop = False
                continue
            elif(userInput == self.__historyMenu[-1].Name()):
                self.__historyMenu.pop()
                continue
            for c in self.__historyMenu[-1].childrens:
                if(userInput == c.Name()):
                    if(isinstance(c, Button)):
                        c.Action()
                        break
                    elif(isinstance(c, ItemContainer)):
                        self.__historyMenu.append(c)
                        break
