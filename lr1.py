import math

#//////////////////// ЗАДАНИЕ 1.5 ////////////////////
# a = int(input())
# b = int(input())
# c = int(input())
# print('Для первого класса' ,a//2+(a%2))
# print('Для второго класса',b//2+(b%2))
# print('Для третьего класса',c//2+(c%2))

#//////////////////// ЗАДАНИЕ 2.11 ////////////////////  alt+shift+e
# a = input("Шахматная доска имеет размер 8x8, введите два числа через пробел, соответствующие клетке начальной точки")
# b = input("Введите клетку конечной точки")
# print(a, b)
# c = a.split(sep=' ')
# n = b.split(sep=' ')
# print(c, n)
#
# if(int(c[0])+2==int(n[0]) and (int(c[1])+1==int(n[1]) or int(c[1])-1==int(n[1]))):
#     print('попадает')
# elif(int(c[0])-2==int(n[0]) and (int(c[1])+1==n[1] or int(c[1])-1==int(n[1]))):
#     print('попадает')
# elif(int(c[1])+2==int(n[1]) and (int(c[0])+2==int(n[0]) or int(c[0])-1==int(n[0]))):
#     print('попадает')
# elif(int(c[1])-2==int(n[1]) and (int(c[0])+2==int(n[0]) or int(c[0])-1==int(n[0]))):
#     print('попадает')
# else:
#     print('не попадает')

#//////////////////// ЗАДАНИЕ 3.6 ////////////////////
# n = int(input('Сколько километров машина проехала за день'))
# m = int(input('Сколько километров нужно проехать'))
# speed = n/24;
# print(math.ceil((m/speed)/24), 'дней нужно, чтобы проехать', m, 'километров')

# #//////////////////// ЗАДАНИЕ 4.5 ////////////////////
# N = int(input('Введите количество чисел'))
# sum = 0
# for i in range(N):
#     a = int(input())
#     sum+=a
# print(sum)


#//////////////////// ЗАДАНИЕ 5.7 ////////////////////
# s = 'jhpphkhl'
# count = s.count('h')
# print(count)
# first = s.find('h')
# last = first
# for i in range(count-1):
#     last = s.find('h', last+1)
# print(first, last)
# s = s.replace(s[first:last], '')
# s = s.replace('h', '')
# print(s)


#//////////////////// ЗАДАНИЕ 6.5 ////////////////////
# sum = 0
# while int(input())!=0:
#     sum+=1
# print(sum)

#//////////////////// ЗАДАНИЕ 7.10 ////////////////////
# sp = [2, 6, 3, 4, 12, 9, 5]
# l = sp.index(min(sp))
# ll = sp.index(max(sp))
# sp[ll], sp[l] = sp[l], sp[ll]
# print(sp)


#//////////////////// ЗАДАНИЕ 8.2 ////////////////////
# def power(a, n):
#     postA = a
#     a/=postA
#     for i in range(n):
#         a /= postA
#     return a
#
# a = int(input())
# n = int(input())
# print(power(a, n))


#//////////////////// ЗАДАНИЕ 9.4 ////////////////////
# def see(a):
#     for row in a:
#         for elem in row:
#             print(elem, end=' ')
#         print()
#     print()
#
# n = int(input())
# a = [[0]*n for i in range(n)]
# see(a)
#
# for k in range(n):
#     for i in range(n-k):
#         a[i][i+k] = k
#
# for k in range(n):
#     for i in range(k, n):
#         a[i][i-k] = k
#
# see(a)


#//////////////////// ЗАДАНИЕ 10.3 ////////////////////
# A = {2, 5, 4, 1, 6, 0}
# B = {2, 4, 3, 9, 1, 0}
# print(A.intersection(B))

#//////////////////// ЗАДАНИЕ 11.2 ////////////////////
# key = ('Hello', 'Bye', 'List')
# value = ('Hi', 'Goodbye', 'Array')
# A = dict(zip(key, value))
#
# v = input()
# if v in A:
#     print(A[v])
# else:
#     print('No')


# #//////////////////// ЗАДАНИЕ 12.7 ////////////////////
# words = dict()
# with open('words.txt') as f:
#     lines = f.read().splitlines()
# for line1 in lines:
#     sum = 0
#     for line in lines:
#         if line1==line:
#             sum+=1
#     words[line1] = sum
#
# maxValue = max(words.values())
# word = {k:v for k, v in words.items() if v == maxValue}
# print(word, maxValue)


