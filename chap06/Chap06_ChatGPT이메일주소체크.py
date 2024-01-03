import re

def check_email(email):
    # 이메일 주소 체크를 위한 정규 표현식 패턴
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # 이메일 주소 검사
    if re.search(pattern, email):
        return True
    else:
        return False

# 테스트용 이메일 주소
email1 = "example@example.com"
email2 = "example@123.com"
email3 = "invalid_email"
email4 = "example@example"
email5 = "example123@example.com"
email6 = "example@.com"
email7 = "example@domain"
email8 = "example@domain."
email9 = "@domain.com"
email10 = "example@@domain.com"

# 이메일 주소 체크
print(check_email(email1))  # True
print(check_email(email2))  # True
print(check_email(email3))  # False
print(check_email(email4))  # False
print(check_email(email5))  # True
print(check_email(email6))  # False
print(check_email(email7))  # False
print(check_email(email8))  # False
print(check_email(email9))  # False
print(check_email(email10))  # False
