#Chap03_forin반복구문.py
value = 5 
while value > 0:
    print(value)
    value -= 1 

#대부분 갯수가 정해져있는 경우
lst = [100,200,300]
for item in lst:
    print(item)

fruit = {"apple":10, "banana":20, "kiwi":30}
for item in fruit.items():
    print(item)

print("key, value를 별도로 처리하는 경우")
for k,v in fruit.items():
    print(k,v)
    