import MenuPropertis
from UI import Item, ItemContainer, Button

class Application:

    def __init__(self, base: dict):
        self.__base = base
        self.__historyMenu = [MenuPropertis.GetMainMenu()]


    def RunApplication(self):
        loop = True
        while(loop):
            print("░" * 20)
            self.__historyMenu[-1].DisplayChildrens()
            userInput = input()

            if(userInput == self.__historyMenu[0].Name()): #Если пользователь вабрал корневой элемент, то завершаем программу
                loop = False
                continue
            elif(userInput == self.__historyMenu[-1].Name()): #Если пользователь вабрал элемент который сейчас активен, то поднимаемся вверх по иерархии
                self.__historyMenu.pop()
                continue
            for c in self.__historyMenu[-1].childrens: #Проходим по дочерним элементам текушего элемента
                if(userInput == c.Name()): #Проверяем этот-ли пункт выбрал пользователь
                    if(isinstance(c, Button)):
                        c.Action()
                        break
                    elif(isinstance(c, ItemContainer)):
                        self.__historyMenu.append(c)
                        break