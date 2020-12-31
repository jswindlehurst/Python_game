import random
import json
import datetime
from operator import itemgetter

def display_menu():
    selection = input("Would you like to A) Play a new game, B) See the best scores, or C) Quit? ")
    return(selection)

def display_score():
    with open("score.txt", 'r') as score_fd:
        scores_list = json.loads(score_fd.read())
        sorted_scores_list = sorted(scores_list, key=itemgetter('score'))
        print(sorted_scores_list[0:3])

def game_level():
    level = input("Would you like to play E) Easy Level, M) Medium Level, or H) Hard Level? ")
    return(level)

def user_name():
    first_name = input("What is your first name?")
    return(first_name)

def play_game(stop_num, level):
    secret_num = random.randint(1,stop_num)
    attempts = 0
    with open("score.txt", 'r') as score_fd:
        scores_list = json.loads(score_fd.read())
    while True:
        guess = int(input("Enter your guess between 1 and "+str(stop_num)+": "))
        if guess > stop_num:
            print("Your guess is larger than the "+str(stop_num)+" limit.  Please play again.")
            break
        else:
            attempts = attempts + 1
            if guess == secret_num:
                print("You are correct and the attempts were", str(attempts))
                first_name = user_name()
                scores_list.append({"first_name": first_name, "score": attempts, "level": level, "datetime": str(datetime.datetime.now())})
                with open("score.txt", 'w') as score_wfd:
                    score_wfd.write(json.dumps(scores_list))
                break
            elif guess < secret_num:
                print("Try a bigger number")
            else:
                print("Try a smaller number")

def main():
    while True:
        selected = display_menu()
        if selected == 'A' or selected == 'a':
            level = game_level()
            if level == 'E' or level == 'e':
                stop_num = 10
            elif level == 'M' or level == 'm':
                stop_num = 30
            else:
                stop_num = 50
            play_game(stop_num, level)
        elif selected == 'B' or selected =='b':
            display_score()
        else:
            print('Exiting the game')
            break

if __name__ == '__main__':
    main()