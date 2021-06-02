# name = input("Enter name :")
#
# print("Name is", name)
#
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = a + b
# print("Sum is", c)

# if statement
# a = 10
# b = 20
#
# if a > b:
#     print("a is greater than b")
#
# if b > a:
#     print("b is greater than a")

# if else statement
# a = 40
# b = 20
# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))
#
# if a > b:
#     print("a is greater than b")
#
# else:
#     print("b is greater than a")

# if elif else statement
# a = 20
# b = 50
#
# if a == b:
#     print("OH WOW!! A & B are equal")
#
# elif a > b:
#     print("a is greater than b")
#
# else:
#     print("b is greater than a")

# nested if statement
# a = int(input("Enter a number: "))
#
# if a != 0:
#     if a > 0:
#         print("a is positive number")
#     else:
#         print("a is negative number")
# else:
#     print("Entered number is 0; neither +ve nor -ve")

# LOOPS

# while loop
# x = 1
#
# while x <= 15:
#     print(x)
#     x += 1

# for loop
# for i in 'Hello people':
#     print("Value is: ", i)
#
# l = [10, 20, 30, 'Hinal', 'Rudra']
#
# print(l)
#
# for i in l:
#     print("Value is ", i)

# for i in range(20):
#     print("Value is: ", i)
#
# for x in range(1,5):
#     print("Value is: ", x)

# for y in range(1,8,2):
#     print("Value is: ", y)

# list = [10, 20, 30, 40, 50, "Hinal"]
# print(list)
#
# for i in list:
#     print("Values is: ", i)
#
# for j in range(len(list)):
#     print("Values is: ", list[j])
#
# else:
#     print("End")

# break and continue
i = 0
while i < 10:
    print("i = ", i)
    i += 1
    if i >= 6:
        break

print("Loop was interuppted.")

# for continue it skips the loop if condition matches

for x in range(20):
    # checks if x is odd, if odd then skips that no and after checking condition it prints the no that is not odd
    if x % 2 != 0:
        continue
    print("x is ", x)

for y in range(10):
    # checks if y is even, if even then skips that no and check the condition again
    if y % 2 == 0:
        continue
    print("Y is ", y)
# condition of odd no then even no are printed
# condition of even no then odd no will be printed

# pass statement
# as we can't keep the body empty we use pass so that it doesnt show syntax error
list1 = [10, 20, 30, 40, 50, "Hinal"]
print(list1)

for i in list1:
    print("Values is: ", i)

for j in range(len(list1)):
    print("Values is: ", list1[j])

else:
    pass
