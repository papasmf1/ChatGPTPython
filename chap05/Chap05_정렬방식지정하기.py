#Chap05_정렬방식지정하기.py
for x in range(1,10):
    print(x,"*",x,"=",x*x)

print("--오른쪽 정렬---")
for x in range(1,10):
    print(x,"*",x,"=", str(x*x).rjust(3)) 

print("--앞쪽에 0으로 채우기---")
for x in range(1,10):
    print(x,"*",x,"=", str(x*x).zfill(3)) 

#문자열형식으로 변환해서 결합연산이 됩니다. 
url = "https://www.python.org/?page=" + str(1) 
print(url)
