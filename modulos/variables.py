camper = list()
def save(data):
    camper.append(data)

def getAll():
    return camper

def eliminate(index):
    value = camper.pop(index)
    return value


