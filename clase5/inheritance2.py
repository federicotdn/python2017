class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def say_hello(self):
        print("My name is:", self._name)
        print("My age is:", self._age)

    def get_birth_year(self):
        return 2017 - self._age

class Professor(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self._subject = subject

    def say_hello(self):
        super().say_hello()
        print("I teach", self._subject)

    def teaches_subject(self, s):
        return self._subject == s

class Student(Person):
    def __init__(self, name, age, exchange):
        super().__init__(name, age)
        self._exchange = exchange

    def say_hello(self):
        super().say_hello()
        if self._exchange:
            print("I am an exchange student")

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

print(isinstance(s, Person))