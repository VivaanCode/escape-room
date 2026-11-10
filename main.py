money = 100
game_room = 1
game_running = True

while game_running:
    if game_room == 1:
        print("Money: "+str(money))
        print("You are stuck in an escape room. What do you do?")
        print("1. Look in the drawer")
        print("2. Jumpscare your best friend Samanyu")
        print("3. Sleep and hope you wake up in a different place.")

        choice1 = input("")

        if choice1 == "1":
            print("You find a dead rat. He steals 20 of your dollars.\nMoney -20")
            money = money - 20
        elif choice1 == "2":
            print("He gets really scared and leaves. You get a refund from the staff. \nMoney +50\n\nMission Passed! Respect+")
            game_room = 2
            money = money + 50
        elif choice1 == "3":
            print("You take a really long nap. Your time runs out and you lose.")
            game_room = 100


    if game_room == 2:
        print("Now that Samanyu is gone, you lost your dead weight. What do you do?")
        print("1. Look inside a light fixture")
        print("2. Look underneath the desk")
        choice2 = input()

        if choice2 == "1":
            print("You find $20! However, the light fixture falls down, and you get kicked out.")
            money = money + 20
            print("Money + 20")
            game_room = 100
        elif choice2 == "2":
            print("You find a key!\n Key+")
            game_room = 3

    if game_room == 3:
        print("You now have a key. What do you do with it?")
        print("1. Try to open the staff room")
        print("2. Use it to leave the escape room")
        print("3. Sand it using the sandpaper in your pocket")

        choice3 = input()

        if choice3 == "1":
            print("It actually opens!")
            game_room = 102
        if choice3 == "2":
            print("The key works!")
            game_room = 101
        if choice3 == "3":
            print("You lose $50 to pay to replace it.\n Money -50")
            money = money - 50
            game_room = 100

    if game_room == 100:
        print("You got kicked out!")
        game_running = False
    if game_room == 101:
        print("You escaped the escape room! Congrats!")
        game_running = False
    if game_room == 102:
        print("You unlocked the SECRET ENDING!!")
        money = money + 500000
        game_running = False

print("\n\nGood game!")
print(f'In this run, you earned {money} dollars!')
print("a game by Vivaan")