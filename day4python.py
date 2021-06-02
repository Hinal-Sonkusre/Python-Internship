# function

# def myfunction():
#     print("Hello world")
#
#
# myfunction()
#
#
# def myfunction1(name):
#     print("Name is:", name)
#
#
# myfunction1("Hinal")


# def myfunction2(name):
#     return name
#
#
# name = myfunction2("Hinal")
# print("Value is ", name)


# def myfunction():
#     name = "Hinal"
#     a = 1
#     return name, a
#
#
# name, a = myfunction()
# print("Name is: ", name)
# print("Value is: ", a)

# default argument
# def sum(a=50, b=50):
#     print(a + b)

# sum(10, 20)
# sum()

# a = int(input("a: "))
# b = int(input("b: "))
# sum(a, b)

# keyword argument
# def sum(a, b):
#     print(a + b)
#
#
# sum(b=20, a=30)

# variable length argument
# non keyword arguments
# def sum(*a):
#     sum = 0
#
#     for i in a:
#         sum += i
#
#     print("Ans is: ", sum)
#
#
# sum(10, 20)
# sum(10, 20, 30)
# sum(10, 10, 10, 10)

# keyword arguments
# def function(**arg):
#     for i,j in arg.items():
#         print(i,j)
#
# function(name = 'Hinal', name2 = 'Rudra')


# variable scope
# def func():
#     x = 5
#     print("x: ", x)
#
# x = 10
# func()
# print("x: ", x)


# modules in python
# import demo
#
# demo.function()

# import demo
#
# name = demo.function("Hinal")
# print("Name is: ", name)


# operators
# arithmetic operators
# a = 5
# b = 5
#
# print("a + b : ", a + b)
# print("a - b : ", a - b)
# print("a * b : ", a * b)
# print("a / b : ", a / b)
# print("a % b : ", a % b)
# print("a // b : ", a // b)
# print("a ** b : ", a ** b)

# comparison operators
# a = 5
# b = 5
#
# print("a > b : ", a > b)
# print("a < b : ", a < b)
# print("a == b : ", a == b)
# print("a != b : ", a != b)
# print("a >= b : ", a >= b)
# print("a <= b : ", a <= b)

# logical operators
# and
# a = 10
# b = 20
# c = 30
#
# if a > b and a > c:
#     print("A is greatest")
#
# elif b > a and b > c:
#     print("B is greatest")
#
# else:
#     print("C is greatest")

# or
# ch = input("Enter a character: ")
#
# if(ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I'  or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
#     print(ch, "is a vowel")
#
# else:
#     print(ch, "is a consonant")

# membership operator
# list = [10, 20, 30, 40]
# x = int(input("x "))
# y = int(input("y "))
#
# print(x in list)
# print((x not in list))
# print(y in list)
# print(y not in list)

# identity operator
a = 10
b = 10

print(a is b)
print(a is not b)