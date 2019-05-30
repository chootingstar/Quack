array = [66, 42, 73, 63, 43, 55, 43]
lastIndex = 1
swapp = True

while swapp == True:
    swapp = False
    lef = 0
    righ = 1
    for i in range(len(array) - lastIndex):
        if array[lef] > array[righ]:
            temp = array[righ]
            array[righ] = array[lef]
            array[lef] = temp
            swapp = True
        lef += 1
        righ += 1
    lastIndex += 1
print(array)