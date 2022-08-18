import random
def generate_numbers(n):
    lotto_number = []
    for i in range(n):
        num = random.randint(1,45)
        lotto_number.append(num)
    return lotto_number