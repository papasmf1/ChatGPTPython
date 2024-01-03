#Chap07_ospath_glob모듈.py
from os.path import * 
from os import * 
import glob 

print("---파일의 전체경로(abspath())---")
print(abspath("python.exe"))
print("---파일 이름만 출력(basename())---")
print(basename("c:\\python310\python.exe"))

print("---python.exe파일이 있다면---")
if exists("c:\\python310\\python.exe"):
    print("파일크기: {0}".format(getsize("c:\\python310\\python.exe")))
else:
    print("파일이 없습니다.")

#특정 파일을 실행할 경우
system("notepad.exe")

print("현재폴더:{0}".format(getcwd()))
chdir("..")
chdir("c:\\work")
print("현재폴더:{0}".format(getcwd()))
lst = glob.glob("*.py")
for item in lst:
    print(item)
