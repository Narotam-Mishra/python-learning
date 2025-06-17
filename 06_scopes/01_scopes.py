
username = "python_and_web"

def func():
    username = "chai"
    print("Inside func:", username)

func()
print("Outside:", username)


x = 99
# def func2(y):
#     z = x + y
#     return z

# res = func2(5)
# print("Result:", res)

# def func3():
#     global x
#     x = 12
    

# func3()
# print("x:", x)

# closures

def f1():
    x = 88
    def f2():
        print("x:", x)
    return f2

myRes = f1()
myRes()

def chaiCode(num):
    def actual(x):
        return x ** num
    return actual


f = chaiCode(2)
g = chaiCode(3)

print("fun1:", f(3))
print("fun2:", g(3))


