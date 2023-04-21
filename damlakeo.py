lbreankfrom random import randint
print("Chao mung den voi Game: Bua, Keo, Bao")

while True:
    print("Chon(Keo, Bua, Bao) hoac nhap End de ket thuc game")
    player = input("Chon: ")
    computer = randint(0,2)
    if computer == 0:
        computer = "Bua"
    if computer == 1:
        computer = "Bao"
    if computer == 2:
        computer = "Keo"

    if player == "Keo":
        if computer == "Bua":
            print("Computer: Bua")
            print("Ban da Thua, Keo < Bua")
        if computer == "Keo":
            print("computer: Keo")
            print("draw")
        if computer == "Bao":
            print("computer: Bao")
            print("Ban da Thang, Keo > Bao")
    if player == "Bua":
        if computer == "Keo":
            print("computer: Keo")
            print("Ban da Thang, Bua > Keo")
        if computer == "Bao":
            print("computer: Bao")
            print("Ban da Thua, Bua < Bao")
        if computer == "Bua":
            print("Computer: Bua")
            print("draw")
    if player == "Bao":
        if computer == "Bao":
            print("computer: Bao")
            print("Draw")
        if computer == "Keo":
            print("computer: Keo")
            print("Ban Da Thua, Bao < Keo")
        if computer == "Bua":
            print("Computer: Bua")
            print("Ban da Thang, Bao > Bua")
    if player == "End":
        print("END GAME, GOODBYE")
        break

print("Dev: Hoang Phuc Nhat Long - Keo Bua Bao Game")

