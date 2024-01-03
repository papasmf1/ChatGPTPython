#Chap03_반복문에서continue_break.py
print("---break---")
lst = list(range(1,11))
print( lst )
for i in lst:
    if i > 5:
        break 
    print("item:{0}".format(i))

print("---continue---")
lst = list(range(1,11))
print( lst )
for i in lst:
    if i % 2 == 0:
        continue
    print(i)

