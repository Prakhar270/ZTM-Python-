from random import randint
import sys

answer = randint(sys.argv[1], sys.argv[2])
while True:
    try:
        number = int(input("Guess the number between 1~10: "))
        if number > 0 and number < 11:
            if number == answer:
                print("Conngo, you guess the write number")
                break
        else:
            print("Input out of limit")
            continue
    except ValueError as err:
        print(f"Opps you enter wrong input {err}")
