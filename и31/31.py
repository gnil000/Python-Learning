def findSum(numsList, length):
    result = []
    suma = 0
    for i in range(length):
        n = 1
        while(n < length):
            suma = numsList[i]
            suma += sum(numsList[i+1:n])
            for j in range(n, length):
                suma += numsList[j]

                # if((suma//50) % 2 != 0):
                if(suma % 100 == 50):
                    result.append(suma)
                suma -= numsList[j]
            n += 1

    return max(result)


directory = 'C:/work/testPython/school/tasks/Лабы/ИЗ1/9/'
A = open(directory+'9a.txt', 'r')
B = open(directory+'9b.txt', 'r')

linesA = A.readlines()
linesB = B.readlines()
numsA = [int(x) for x in linesA]
numsB = [int(x) for x in linesB]
lenA = len(numsA)
lenB = len(numsB)


maxA = findSum(numsA, lenA)
maxB = findSum(numsB, lenB)
# print(maxA)
print(maxA, maxB)
if maxA > maxB:
    print(maxA)
else:
    print(maxB)
