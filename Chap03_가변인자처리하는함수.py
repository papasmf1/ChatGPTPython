#Chap03_가변인자처리함수.py
#가변인자(갯수가 정해져 있지 않은경우)
def union(*tp):
    result = []
    for item in tp:
        for x in item:
            if x not in result:
                result.append(x)
    return result  

print( union("HAM","SPAM") )
print( union("HAM","SPAM","EGG") )


