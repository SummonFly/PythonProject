from abc import ABC, abstractmethod

class IElement(ABC):

    def SetParent(self, parent):
        self.__parent = parent


    def GetParent(self):
        return  self.__parent


    @abstractmethod
    def Display(self):
        pass


    @abstractmethod
    def Name(self) -> str:
        pass



class Item(IElement):

    def __init__(self, name: str, parent = None):
        self.__name = name
        self.SetParent(parent)


    def Display(self):
        print(f'\t', self.__name)


    def Name(self) -> str:
        return self.__name



class ItemContainer(IElement):

    def __init__(self, name: str, parent = None):
        self.__name = name
        self.childrens = []
        self.SetParent(parent)


    def Display(self):
        print(self.__name)
        for it in self.childrens:
            print(f'\t', end=' ')
            it.Display()


    def DisplayChildrens(self):
        print(self.__name)
        for it in self.childrens:
            print(f'\t', end=' ')
            print(it.Name())


    def Name(self) -> str:
        return self.__name


    def AddChildren(self, e: IElement):
        e.SetParent(self)
        self.childrens.append(e)


    def RemoveChildren(self, e: IElement):
        e.SetParent(None)
        self.childrens.remove(e)


    def Clear(self):
        for c in self.childrens:
            c.SetParent(None)
        self.childrens = []

class Button(Item):
    def __init__(self, name: str, act):
        super().__init__(name)
        self.Action = act