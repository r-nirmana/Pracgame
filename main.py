import random

COLORS = ["R","G","B","Y","W","O"]
TRIES = 10
CODE_LENGTH = 4

code = []

def generate_codes():
    for i in range(CODE_LENGTH):
        COLOR = random.choice(COLORS)
        code.append(COLOR)

    return code

def guess_code():

    while True:

        guess = input("Guess : ").upper().split(" ")

        if len(guess) != 4:
            print(f"please guess {CODE_LENGTH} colours")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid Color {color}..Try again")
                break

        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    


