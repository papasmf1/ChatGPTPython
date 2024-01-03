#Chap06_정규표현식.py 
import re 

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())
result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())

#함정이 추가된 경우
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

print("---특정 단어를 찾는 경우---")
result = re.search("apple", "빅테크에서 apple의 위상")
print(result.group())
print("---연도를 찾는경우---")
result = re.search("\d{4}", "올해는 2023년")
print(result.group())
print("---우편번호를 찾는경우---")
result = re.search("\d{5}", "우리동네는 52100")
print(result.group())

print("---대소문자를 모두 찾는 경우---")
data = "Apple id big company and apple is very delicious"
c = re.compile("apple", re.IGNORECASE)
print(c.findall(data))

print("---다중 라인을 전부 검색할 경우---")
data = """파이썬은 
누구나 쉽게 배워서 

사용할 수 있는 멋진 언어입니다."""
c = re.compile("^.+", re.MULTILINE)
print(c.findall(data))
