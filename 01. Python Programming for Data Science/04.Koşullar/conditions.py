# Koşullar (Conditions)
"""
- Akış konrolü yapmak için kullanılır.
- Eğer bu şart sağlanıyorsa bu işlemi yap, değilse bu işlemi yap.

"""

# True / False

1 == 1
1 == 2

# if
"""
if koşul:
    koşul sağlandığında yapılacak işlem
"""
if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

number = 11
if number == 10:
    print("number is 10")

number = 10


def number_check(number):
    if number == 10:
        print("number is 10")

number_check(10)

# else

"""
if koşul:
    koşul sağlandığında yapılacak işlem
else:
    koşul sağlanmadığında yapılacak işlem
"""

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(12)

# elif
"""
if koşul:
    koşul sağlandığında yapılacak işlem
elif koşul2:
    koşul2 sağlandığında yapılacak işlem
else:
    koşullar sağlanmadığında yapılacak işlem
"""

def number_check(number):
    if number > 10:
        print("number is greater than 10")
    elif number < 10:
        print("number is less than 10")
    else:
        print("equal to 10")
number_check(12)
