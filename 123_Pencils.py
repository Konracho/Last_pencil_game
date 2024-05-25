import random
import sys

def John_player(pencils_start):
    print('|' * pencils_start)
    print(f"John's turn")
    John_take_a_pencil = input()
    while John_take_a_pencil.isdigit() == False or int(John_take_a_pencil) > 3 or int(John_take_a_pencil) == 0:
        print("Possible values: '1', '2' or '3'")
        John_take_a_pencil = input()
    while int(John_take_a_pencil) > pencils_start:
        print("Too many pencils were taken")
        John_take_a_pencil = input()
    else:
        pencils_start = pencils_start - int(John_take_a_pencil)
        if pencils_start >= 1:
            # pencils_start = pencils_start - int(John_take_a_pencil)
            Jack_player_bot(pencils_start)
            print("Jack won!")
            sys.exit()

        elif pencils_start == 0:
            print("Jack won!")
            sys.exit()

        else:
            print('|' * pencils_start)
            pencils_start = pencils_start - int(John_take_a_pencil)

    Jack_player_bot(pencils_start)

def Jack_player_bot(pencils_start):
    print('|' * pencils_start)
    print(f"Jack's turn")

    if pencils_start in range(5, pencils_start + 1, 4):
        Jack_take_a_pencil = random.randrange(1, 3, 1)
        Jack_take_a_pencil = int(Jack_take_a_pencil)
        print(Jack_take_a_pencil)
        pencils_start = pencils_start - Jack_take_a_pencil

    elif pencils_start in range(4, pencils_start + 1, 4):
        Jack_take_a_pencil = 3
        print(Jack_take_a_pencil)
        pencils_start = pencils_start - int(Jack_take_a_pencil)

    elif pencils_start in range(3, pencils_start + 1, 4):
        Jack_take_a_pencil = 2
        print(Jack_take_a_pencil)
        pencils_start = pencils_start - int(Jack_take_a_pencil)

    elif pencils_start in range(2, pencils_start + 1, 4):
        Jack_take_a_pencil = 1
        print(Jack_take_a_pencil)
        pencils_start = pencils_start - int(Jack_take_a_pencil)

    elif pencils_start == 1:
        print(pencils_start)
        print("John won!")
        sys.exit()

    John_player(pencils_start)

def game():
    print('How many pencils would you like to use:')
    pencils_start = input()

    while pencils_start.isdigit() == False:
        print('The number of pencils should be numeric')
        pencils_start = input()

    while int(pencils_start) < 0:
        print("The number of pencils should be numeric")
        pencils_start = input()
        while pencils_start.isdigit() == False:
            print('The number of pencils should be numeric')
            pencils_start = input()

    while int(pencils_start) == 0:
        print("The number of pencils should be positive")
        pencils_start = input()
        while pencils_start.isdigit() == False:
            print('The number of pencils should be numeric')
            pencils_start = input()

    else:
        pencils_start = int(pencils_start)

    print('Who will be the first (John, Jack):')
    name = str(input())

    while name != "John" and name != "Jack":
        print(f"Choose between John and Jack")
        name = str(input())

    if name == "John":
        John_player(pencils_start)

    elif name == "Jack":
        Jack_player_bot(pencils_start)

game()

