print("Hello, "+" World")
print(3**2-4*1*2)
print("a"+"a"+"a"+"a")
print(12 == 12//5*5+12%2)
print(12 == 5*12//5+12%2)

#task4
my_var = 2
print(my_var)

v1 = 20
v2 = "20"
v3 = 2*v1#40
v4 = 2*v2#2020
print(v3, v4)
print(v2+v2)#2020

v1 = v2+v2#2020
print(v1+v2)#202020


my_var1 = "twenty"
print(my_var1)#twenty
my_var2 = my_var1#twenty
my_var1 = 5
print(my_var2)#twenty
print(my_var1, my_var2)#5twenty


def func1(my_var):
    print(my_var)
    return my_var

my_var = "CSCA08"
print(my_var) #CSCA08

my_var = func1(my_var)
print(my_var)#CSCA08


def student_data(name, age, student_num, in_2152):
    """

    name: student's name: string
    age:student's age: int, always > 0
    student_num: string
    in_2152: boolean, True if and only if student is enrolled in 2152
    return:  a string representation of their data, in the order
of student number, name, age and enrolment status.

    """




N = int(input("What is your number?"))

if N >= 1 & N <= 100:
    if N % 2 != 0:
        print("Weird")
    elif N % 2 == 0:
        if N >= 2 | N <= 5:
            print("Not Weird")
        elif N % 2 == 0 and 6 <= N <= 20:
            print("Weird")
        elif N > 20:
            print("Not Weird")
