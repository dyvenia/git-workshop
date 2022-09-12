# Facu's script


x = 25

numList = [i for i in range(x)]
numList += [i for i in range(x, -1, -1)]


for i in numList:
    print("*" * i * 2)
