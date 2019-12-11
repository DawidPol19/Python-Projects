# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 12:21:24 2019

@author: Lofu
"""

x = [[1,2,3], [4,5,6]]

#print(x[0][0])

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

def snail(array):
    f = []
    while array != []:
        if array != []:
            for i in array[0]:
                f.append(i)
            array.remove(array[0])
        else:
            return f

        if array != []:
            for i in array:
                f.append(i[len(i) - 1])
                i.remove(i[len(i) - 1])
        else:
            return f

        if array != []:
            array[len(array) - 1] = array[len(array) - 1][::-1]
            for i in array[len(array) - 1]:
                f.append(i)
            array.remove(array[len(array) - 1])
        else:
            return f

        if array != []:
            array = array[::-1]
            for i in array:
                f.append(i[0])
                i.remove(i[0])
            array = array[::-1]
        else:
            return f
    return f

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

a = [[1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]]
b = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

def snailu(array):
    l, lt, c, x0, x1 = [], int(len(array[0])/2),0, 0, len(array[0]) - 1 # 4
    while c <= lt:
        for i in range(x0,(x1 + 1)):
            l.append(array[x0][i]) 
        for i in range((x0 + 1),(x1 + 1)):
            l.append(array[i][x1])
        for i in range((x1 - 1),(x0 - 1), -1):
            l.append(array[x1][i])
        for i in range((x1 - 1),x0, -1):
            l.append(array[i][x0])
        x0 += 1
        x1 -= 1
        c += 1
    return l

print(snailu(b))






