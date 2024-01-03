#Chap04_부모클래스_자식클래스_변경.py
#부모클래스 정의 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
    def working(self):
        print("지금 일하고 있음")
    def sleep(self):
        print("지금 잠자고 있음")

#자식클래스 정의 
class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모의 생성자메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받은 메서드를 재정의(덮어쓰기) 
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(
            self.subject, self.studentID))

#인스턴스 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터학과", "230123")
p.printInfo()
s.working()
s.sleep() 


