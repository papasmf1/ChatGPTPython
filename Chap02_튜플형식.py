#Chap02_튜플형식.py
tp = (100, 200, 300)
print( len(tp) )
print( tp.index(200) )
print( tp.count(300) )
print("id: %s, name: %s" % ("kim","김유신"))

#함수 정의
def times(a,b):
    return a+b, a*b 

#호출
result = times(3,4)
print(result)
