class Professor:
    def __init__(self, name, age, subject):
        self._name = name
        self._age = age
        self._subject = subject

    def say_hello(self):
        print("My name is:", self._name)
        print("My age is:", self._age)
        print("I teach", self._subject)

    def get_birth_year(self):
        return 2017 - self._age

    def teaches_subject(self, s):
        return self._subject == s

class Student:
    def __init__(self, name, age, exchange):
        self._name = name
        self._age = age
        self._exchange = exchange

    def say_hello(self):
        print("My name is:", self._name)
        print("My age is:", self._age)
        if self._exchange:
            print("I am an exchange student")

    def get_birth_year(self):
        return 2017 - self._age

    def is_exchange_student(self):
        return self._exchange

p = Professor("John", 44, "maths")
p.say_hello()
print(p.get_birth_year())
print(p.teaches_subject("computer science"))

s = Student("Mike", 17, True)
s.say_hello()
print(s.get_birth_year())
print(s.is_exchange_student())