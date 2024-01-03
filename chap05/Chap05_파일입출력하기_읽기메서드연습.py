#Chap05_파일입출력하기_읽기메서드연습.py
print("---파일쓰기---")
f = open("c:\\work\\test.txt", "wt")
f.write("첫번째\n두번째\n세번째\n")
f.close() 

print("---파일읽기---")
f = open("c:\\work\\test.txt", "rt")
print("---read()메서드호출--")
result = f.read() 
print(result)

print("---readline()메서드호출--")
#파일포인터를 다시 처음으로 이동
f.seek(0)
print( f.readline(), end="" )
print( f.readline(), end="" )

print("---readlines()메서드호출--")
f.seek(0)
lst = f.readlines()
print(lst)
for item in lst:
    print(item, end="")
    
#읽기 작업이 다 끝나면 마지막에 닫기 
f.close() 