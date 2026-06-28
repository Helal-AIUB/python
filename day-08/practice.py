# class Student:
#     college_name = "ABC College"
#     def __init__(self):
#         pass
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#     def welcome(self):
#         print("Welcome Student", self.name)

# s1 = Student("Rozhan", 89)
# print(s1.name, s1.marks)
# print(Student.college_name)
# s1.welcome()

# s2 = Student("ABC", 79)
# print(s2.name, s2.marks)
# print(s2.college_name)
# s2 = Student()
# print(s2.name)

# class Car:
#     color = "blue"
#     brand = "mercedes"
# car1 = Car()
# print(car1.color)
# print(car1.brand)


# -----------------------------PRACTICE QUESTION-------------------------------

# class Student:
#     def __init__(self,name, marks):
#         self.name = name
#         self.marks = marks

#     def avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi, ",self.name,"Your avg marks: ",sum/3)
# s1 = Student("Faravi",[89,56,78])
# s1.name = "ABCDKDKD"
# s1.avg()


#--------------------------------ABSTRUCTION--------------------------

# class Car:
#     def __init__(self):
#         self.acce = False
#         self.brk = False
#         self.clutch = False
#     def Start(self):
#         self.clutch = True
#         self.acce = True
#         print("Car started...")
# car1 = Car()
# car1.Start()


# Create an Account with 2 attributes and write methods
# class Account():
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.acc_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("BDT,",amount,"was debited successfully.")
#         print("Total Balance: ", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("BDT,",amount,"was creadited successfully.")
#         print("Total Balance: ", self.get_balance())
    
#     def get_balance(self):
#         return self.balance


# acc1 = Account(10000, 12345)
# acc1.debit(5000)
# acc1.credit(10000)

#--------------------------Object Delete - del ------------------------

# class Student():
#     def __init__(self, name):
#         self.name = name
# s1 = Student("Rozhan")
# print(s1.name)
# del s1.name
# print(s1.name)

#------------------------PRIVATE-------------------------------
# class Account():
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)      # We can access here (within class)
# s1 = Account(12345, "abcde")
# print(s1.acc_no)
# s1.reset_pass()
# print(s1.__acc_pass)       # We can not access here(outside class)


# class Person():
#     __name = "anonymous"

#     def __hello(self):
#         print("Hello User")
#     def welcome(self):
#         self.__hello()

# p1 = Person()
# p1.welcome()


# ----------------------------------Multi-level Inheritance-----------------------------
# class Car():
#     @staticmethod
#     def start():
#         print("Car started...")
#     @staticmethod
#     def stop():
#         print("Car stopped...")
# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand


# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()


# car1 = ToyotaCar("fortune")
# car2 = ToyotaCar("previous")
# print(car1.name)
# car1.start()


# ----------------------------------Multiple Inheritance-----------------------------
# class A():
#     varA = "Welcome to class A"

# class B(A):
#     varB = "Welcome to class B"

# class C(B, A):
#     varC = "Welcome to class C"
# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

#----------------------------------------Super()----------------------------------
# class Car():
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("Car started...")
#     @staticmethod
#     def stop():
#         print("Car stopped...")
# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)

# car1 = ToyotaCar("abc","electric")
# print(car1.type)


#---------------------------------------Class Method---------------------------------
# class Person():
#     name = "annonymous"

#     # def changeName(self, name):
#     #     self.__class__.name = name
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Rahul Kumar")
# print(p1.name)
# print(Person.name)


# class Student():
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         # self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3) + "%"

# stu1 = Student(89,90,78)
# print(stu1.percentage)

# stu1.phy = 50
# print(stu1.percentage)

#-----------------------Polymorphism(multiple form)------------------------
# print( 3 + 3)
# print("Apna" + "college")
# print([2,3,4] + [5,6,7])


class Complex():
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.showNumber()
num2 = Complex(4,6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()