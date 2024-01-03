#Chap03_ifelse.py

score = int(input("점수를 입력:"))
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grace = "F"
    
print("등급은 " + grade)
