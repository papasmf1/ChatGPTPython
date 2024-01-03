#Chap05_파일입출력하기.py
print("---파일쓰기---")
f = open("c:\\work\\test.txt", "wt")
f.write("첫번째\n두번째\n세번째\n")
f.close() 

print("---파일읽기---")
f = open("c:\\work\\test.txt", "rt")
result = f.read() 
print(result)
f.close() 