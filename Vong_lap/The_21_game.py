from random import randint
from random import choice
while True:
    current_player = choice(["Player", "Computer"])
    print("New game!")
    print(f"Now is {current_player} turn.")
    print("_________________________________")
    result = None
    current_num = 0
    while True:
        if current_player == "Player":
            player_chose = int(input("Please choose 1, 2 or 3: "))
            while player_chose not in [1, 2, 3]:
                player_chose = int(input("Please choose 1, 2 or 3: "))
            current_num += player_chose
            print(f"{current_player} chose {player_chose}. The number is {current_num}")
            if current_num >= 21:
                result = "LOSE"
                print(f"{current_player} has reached {current_num}, you {result}")
                print("_________________________________")
                break
            else:
                current_player = "Computer"
        else:
            com_chose = randint(1,3)
            current_num += com_chose
            print(f"{current_player} chose {com_chose}. The number is {current_num}")
            if current_num >= 21:
                result = "WIN"
                print(f"{current_player} has reached {current_num}, you {result}")
                print("_________________________________")
                break
            else:
                current_player = "Player"
    if result == "LOSE":
        continue
    else:
        play_again = str(input("Do you want to play again? y/n: "))
        while play_again not in ["y", "n"]:
            play_again = str(input("Do you want to play again? y/n: "))
        if play_again == "y":
            continue
        else:
            break
print()
print("Game over!")