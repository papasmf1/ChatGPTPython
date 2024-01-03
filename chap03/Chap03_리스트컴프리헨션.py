#Chap03_리스트컴프리헨션.py
#리스트컴프리헨션
lst = list(range(1,11))
print( [i**2 for i in lst if i >5] )

fruits = ("apple", "banana", "kiwi")
print( [len(i) for i in fruits] )

fruits2 = {100:"apple", 200:"banana", 300:"kiwi"}
print( [v.upper() for v in fruits2.values()] )

