def oldMcDonald(animal, sound):
    str1 = "Old McDonald had a {0}. Eyi Eyi oh."\
           "And on his farm he had a {0}. Eyi Eyi oh."\
           "With a {1} {1} here, and a {1:} {1:} there."\
           "Here {1:}, there {1:}, everywhere a {1:} {1:}."\
           "Old McDonald had a farm. Eyi Eyi oh.".format(animal, sound)
    return str1


def xor(a, b):
    """
    (true, true)->true
    (false, true)->false
    (true, false)->false
    (false, false)->true


    :param a:
    :param b:
    :return:
    """
    return not a or b

def factorial(n):
    f = 1
    i = 1
    while i <= n:
        f = f*i
        i = i+1
    return f


def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if (x % y) == 0:
                return "not prime"
    else:
        return "prime"
    return "prime"


print(is_prime_number(r))
print(oldMcDonald("Cow", "moo"))
print(xor(False, False))

a = int(input("Enter a natural number > 1: "))
r = (factorial(a-1)+1)

print(r)



