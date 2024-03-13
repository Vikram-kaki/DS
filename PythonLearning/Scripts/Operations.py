def find_average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0


def filter_even(numbers):
    return [x for x in numbers if x % 2 == 0]


def reverse_list(numbers):
    return numbers[::-1]


def concatenate_list(lst1, lst2):
    return lst1 + lst2
