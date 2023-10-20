def FilterValue(base: dict, filter):
    result = dict()
    for key in base.keys():
        if(filter(base[key])):
            result[key] = base[key]
    return result


def FilterKey(base: dict, filter):
    result = dict()
    for key in base.keys():
        if(filter(key)):
            result[key] = base[key]
    return result

def GetMaxValue(base: dict):
    maxValue = (0, 0)
    for key in base.keys():
        if(base[key] > maxValue[1]):
            maxValue = (key, base[key])
    return maxValue


def GetMinValue(base: dict):
    minValue = (0, GetMaxValue(base)[1])
    for key in base.keys():
        if(base[key] < minValue[1]):
            minValue = (key, base[key])
    return minValue


def GetAverage(base: dict):
    average = 0
    for key in base.keys():
        average += base[key]
    return average / len(base.keys())


def AddNewAdmin(base: dict, admin: str, payments: int):
    base[admin] = payments


def RemoveAdmin(base: dict, admin: str):
    base.pop(admin)


