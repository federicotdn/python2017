def f1():
    f2()

def f2():
    f3()

def f3():
    raise Exception("ERROR!")

try:
    f1()
except:
    print("Error manejado")

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Error!')
    finally:
        print('Executing finally clause.')

print(divide(1,1))
print(divide(1,0))