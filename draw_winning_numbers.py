import generate_numbers
def draw_winning_numbers():
    win_num = generate_numbers(7)
    return sorted(win_num[:6]) + win_num[6:]
print(draw_winning_numbers())