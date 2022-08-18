from .count_matching_numbers import count_matching_numbers


def check(numbers,winning_numbers):
    count = count_matching_numbers(numbers,winning_numbers[:6])
    bounus_count = count_matching_numbers(numbers,winning_numbers[6:])
    if count == 6:
        return 10000000000
    elif count == 5 and bounus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0