#Chap06_문자열처리메서드.py
strA = "파이썬은 강력해"
strB = "python is very powerful"

print("---문자열의 길이 출력---")
print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.count("p"))
print(strB.count("p",7))

print("---시작패턴과 끝패턴을 체크---")
print(strB.startswith("python"))
print(strB.endswith("ful"))

print("---대문자로 변환하고 소문자로 변환---")
result = strB.upper()
print(result)
print(result.lower())

print("---알파벳과 숫자로만 구성되어 있는지---")
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

print("---앞뒤에 있는 불필요한 문자열 잘라내기---")
data = "<<<  피자 햄버거 치킨  >>>"
result2 = data.strip("<> ")
print(result2)

print("---문자열을 치환하기---")
result3 = result2.replace("피자", "피자 콜라")
print(result3)

print("---문자열을 리스트로 변환하고 다시 합치기---")
lst = result2.split()
print("list:{0}".format(lst))
result3 = " ".join(lst)
print("다시 하나로 조립:{0}".format(result3))
