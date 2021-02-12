def count(x, string):
    counter = 0
    for i in string:
        if i == x:
            counter = counter + 1
        else:
            pass

    return counter

def my_in(i, li):
    '''
    '''
    for item in li:
        return item == i

def indexer(i, list):
    #this doesn't work lol
    for item in list:
        if item == i:
            return list[0:i]
            continue
        elif item != i:
            pass

days = ['Mo', 'Tu', 'We', 'Th'] # keys
temps = [55, 23, 42, 44] # values

def createTempD(days, temps):
    result = {}
    for key in days:
        for value in temps:
            result[key] = value
            temps.remove(value)
            break

    return result
