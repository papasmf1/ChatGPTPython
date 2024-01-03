#Chap02_딕셔너리.py 
device = {"아이폰":5, "아이패드":10, "윈도우노트북":20}
print( device )
print( type(device) )
print( len(device) )

#검색
print( device["아이폰"] )
#입력
device["맥북"] = 15 
#수정
device["아이폰"] = 6 
#삭제
del device["아이패드"]
print( device )

#참조를 복사해서 전달한다.
phone = {"kim":"010-111-2222", "lee":"010-123-1234",
    "park":"010-222-3333"}
print( phone )
print("포함 여부 체크:", "park" in phone)
print("포함되어 있지 않은 경우 체크:", "moon" not in phone)

p = phone
print( id(phone), id(p) )
p["moon"] = "010-1234-5678"
print( phone )
print( p )
