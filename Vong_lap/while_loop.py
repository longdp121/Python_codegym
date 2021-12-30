from random import randint
#Khai bao bien player

result = None
#while True:

while result != "Thang":
    #Khai bao bien player
    player = str(input())
    if player != "1" and player != "2" and player != "3":
        print("Nhap sai")
    elif player == "1" or player == "2" or player == "3":
        if player == "1":
            player_choose = "Dam"
        elif player == "2":
            player_choose = "La"
        elif player == "3":
            player_choose = "Keo"

        #Khai bao bien com
        com = randint(1,3)
        if com == 1:
            com_choose = "Dam"
        elif com == 2:
            com_choose = "La"
        elif com == 3:
            com_choose = "Keo"

        #Khai bao result
        if player_choose == com_choose:
            result = "Hoa"

        elif player_choose == "Dam":  #Player chon Dam__1
            if com_choose == "La":
                result = "Thua"
            else:
                result = "Thang"

        elif player_choose == "La":  #Player chon La__2
            if com_choose == "Keo":
                result = "Thua"
            else:
                result = "Thang"

        elif player_choose == "Keo":  #Player chon Dam__3
            if com_choose == "Dam":
                result = "Thua"
            else:
                result = "Thang"
        print(f"Nguoi choi chon {player_choose}, may tinh chon {com_choose}, ket qua: {result}")
    else:
        continue
print("GAME OVER")
