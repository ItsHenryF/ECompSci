import math
from os import read
kcTemp = []
kcPress = []
kcDesc = []
with open("KC.txt") as f:
    reader = f.read()
    temp = reader.split('"temp":')
    press = reader.split('"pressure":')
    desc = reader.split('"description":"')
    i = 1
    while True:
        try:
            pressReader = (press[i].split(","))
            tempReader = (temp[i].split(','))
            descReader = (desc[i].split('"'))
            kcTemp.append(tempReader[0])
            kcPress.append(pressReader[0])
            kcDesc.append(descReader[0])
            i+=1
        except:
            break
i = 0
counter = 1
print("Num     Temp      Pressure       Description")
print("-"*50)
while i < len(kcTemp):
    print("#{:<2})".format(counter),"{:<2}".format(" "),'{:<10.2f}'.format(round(float(kcTemp[i]),2)),end="")
    print('{:<15}'.format(kcPress[i]), end="")
    print('{:<15}'.format(kcDesc[i]))
    i+=1
    counter+=1