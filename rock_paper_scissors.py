import random
import time
pointsGamer = 0
pointsBot = 0
while True:
    choice = ["R", "P", "S"]
    bot = random.choice(choice)
    gamer = str(input("Rock, Paper or Scissors?  (R=Rock, P=Paper, S=Scissors) "))

# Rock
    if bot == "R" and gamer.lower().strip() == "r":
        time.sleep(0.5)
        print("the bot also chose rock, so it's a tie")
        print("your points:", pointsGamer, "bot points:", pointsBot)
        next = (input("Wanna play again? (Y/N) "))
        if next.lower().strip() == "n":
            break
        if next.lower().strip() != "y":
            print("really?")
            break

    elif bot == "R" and gamer.lower().strip() == "p":
        time.sleep(0.5)
        print("the bot chose rock and  you chose paper, so.. you win!")
        pointsGamer += 1
        print("your points:", pointsGamer, "bot points:", pointsBot)
        next = str(input("Wanna play again? (Y/N) "))
        if next.lower().strip() == "n":
            break
        if next.lower().strip() != "y":
            print("really?")
            break

    elif bot == "R" and gamer.lower().strip() == "s":
        time.sleep(0.5)
        print("the bot chose rock and you chose scissors, so... you lose....")
        pointsBot += 1
        print("your points:", pointsGamer, "bot points:", pointsBot)
        next = str(input("Wanna play again? (Y/N) "))
        if next.lower().strip() == "n":
            break
        if next.lower().strip() != "y":
            print("really?")
            break
    # paper
    if bot == "P" and gamer.lower().strip() == "p":
        time.sleep(0.5)
        print("the bot also chose paper, so it's a tie")
        print("your points:", pointsGamer, "bot points:", pointsBot)
        next = str(input("Wanna play again? (Y/N) "))
        if next.lower().strip() == "n":
            break
        if next.lower().strip() != "y":
            print("really?")
            break
    elif bot == "P" and gamer.lower().strip() == "s":
        time.sleep(0.5)
        print("the bot chose paper and you chose scissors, so.... you win!")
        pointsGamer += 1
        print("your points:", pointsGamer, "bot points:", pointsBot)
        next = str(input("Wanna play again? (Y/N) "))
        if next.lower().strip() == "n":
            break
        if next.lower().strip() != "y":
            print("really?")
            break
    elif bot == "P" and gamer.lower().strip() == "r":
        time.sleep(0.5)
        print("the bot chose paper and you chose rock, so.... you lose...")
        pointsBot += 1
        print("your points:", pointsGamer, "bot points:", pointsBot)
        next = str(input("Wanna play again? (Y/N) "))
        if next.lower().strip() == "n":
            break
        if next.lower().strip() != "y":
            print("really?")
            break
    # Scissors
    if bot == "S" and gamer.lower().strip() == "s":
        time.sleep(0.5)
        print("the bot also chose scissors, so it's a tie")
        print("your points:", pointsGamer, "bot points:", pointsBot)
        next = str(input("Wanna play again? (Y/N) "))
        if next.lower().strip() == "n":
            break
        if next.lower().strip() != "y":
            print("really?")
            break
    elif bot == "S" and gamer.lower().strip() == "r":
        time.sleep(0.5)
        print("the bot chose scissors and you chose rock, so.... you win!")
        pointsGamer += 1
        print("your points:", pointsGamer, "bot points:", pointsBot)
        next = str(input("Wanna play again? (Y/N) "))
        if next.lower().strip() == "n":
            break
        if next.lower().strip() != "y":
            print("really?")
            break
    elif bot == "S" and gamer.lower().strip() == "p":
        time.sleep(0.5)
        print("the bot chose scissors and you chose paper, so... you lose...")
        pointsBot += 1
        print("your points:", pointsGamer, "bot points:", pointsBot)
        next = str(input("Wanna play again? (Y/N) "))
        if next.lower().strip() == "n":
            break
        if next.lower().strip() != "y":
            print("really?")
            break
if pointsBot > pointsGamer:
    print("bot won!")
    time.sleep(2)
elif pointsBot == pointsGamer:
    print("it's a tie!")
    time.sleep(2)
else:
    print("you won!")
    time.sleep(2)
