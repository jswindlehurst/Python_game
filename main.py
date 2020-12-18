import random
secret_num = random.randint(1,50)
attempts = 0
while True :
    guess = int(input ("Enter your guess between 1 and 50.  To quit, enter 0:" ))
    if guess == 0:
        break
    attempts = attempts + 1
    if guess == secret_num :
        print("You are correct and the attempts were", str(attempts))
        attempts = 0
        secret_num = random.randint(1, 50)
    elif guess < secret_num:
        print("Try a bigger number")
    else :
        print("Try a smaller number")

print("You have exited the game")