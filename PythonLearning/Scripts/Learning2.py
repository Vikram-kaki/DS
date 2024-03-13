# def convert_to_decimal(binary_number):
#     decimal_number = 0
#     two_power = 0
#
#     while binary_number > 0:
#         temp = binary_number % 10
#         decimal_number = decimal_number + (temp * (2 ** two_power))
#         two_power += 1
#         binary_number //= 10
#
#     return decimal_number
#
#
# print(convert_to_decimal(10101))


# A program to convert a decimal number to binary

def convert_to_binary(decimal_number):
    binary_number = 0
    two_power = 0

    while decimal_number > 0:
        temp = decimal_number % 2
        binary_number = binary_number + (temp * (10 ** two_power))
        two_power += 1
        decimal_number //= 2

    return binary_number


print(convert_to_binary(83))
print(convert_to_binary(10))
print(convert_to_binary(11))
print(convert_to_binary(12))


# A program to find the given numbers are coprime or not

def coprime(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b

    return a


print(coprime(10, 15))