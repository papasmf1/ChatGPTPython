#Chap04_ChatGPT클래스생성코드.py 
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print("ID:", self.id)
        print("Name:", self.name)


class Manager(Person):
    def __init__(self, id, name, skill, title):
        super().__init__(id, name)
        self.skill = skill
        self.title = title


class Employee(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title


class Alba(Person):
    pass


# 인스턴스 생성 및 메서드 호출
person = Person(1, "John Doe")
person.printInfo()

print()

manager = Manager(2, "Jane Smith", "Leadership", "Senior Manager")
manager.printInfo()
print("Skill:", manager.skill)
print("Title:", manager.title)

print()

employee = Employee(3, "Michael Johnson", "Software Engineer")
employee.printInfo()
print("Title:", employee.title)

print()

alba = Alba(4, "Kim Young")
alba.printInfo()
