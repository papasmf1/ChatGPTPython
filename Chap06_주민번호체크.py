#Chap06_주민번호체크.py
import re

def check_korean_id(id_num):
    # 주민번호 체크를 위한 정규 표현식 패턴
    pattern = r'^\d{6}-[1-2]\d{6}$'

    # 주민번호 검사
    if re.search(pattern, id_num):
        return True
    else:
        return False

# 테스트용 주민번호
id_num1 = "830101-1234567"
id_num2 = "910202-1234567"
id_num3 = "990303-1234567"
id_num4 = "051010-1234567"
id_num5 = "020505-1234567"
id_num6 = "970707-1234567"
id_num7 = "810808-1234567"
id_num8 = "123456-1234567"
id_num9 = "901231-123456"
id_num10 = "870510-abcdefg"

# 주민번호 체크
print(check_korean_id(id_num1))  # True
print(check_korean_id(id_num2))  # True
print(check_korean_id(id_num3))  # True
print(check_korean_id(id_num4))  # True
print(check_korean_id(id_num5))  # True
print(check_korean_id(id_num6))  # True
print(check_korean_id(id_num7))  # True
print(check_korean_id(id_num8))  # False
print(check_korean_id(id_num9))  # False
print(check_korean_id(id_num10))  # False
