logo = '''

                                _    _                                      _                 
  __ _  _   _   ___  ___  ___  | |_ | |__    ___   _ __   _   _  _ __ ___  | |__    ___  _ __ 
 / _` || | | | / _ \/ __|/ __| | __|| '_ \  / _ \ | '_ \ | | | || '_ ` _ \ | '_ \  / _ \| '__|
| (_| || |_| ||  __/\__ \\__ \ | |_ | | | ||  __/ | | | || |_| || | | | | || |_) ||  __/| |   
 \__, | \__,_| \___||___/|___/  \__||_| |_| \___| |_| |_| \__,_||_| |_| |_||_.__/  \___||_|   
 |___/                                                                                        
                                                                                                                      
'''

from random import randint
# choose level
def level():
    Level= input("choose a level : hard or easy?\n")
    if Level == "hard":
        print("you have 5 attempts")
        return 5
    elif Level =="easy":
        print("you have 10 attempts")
        return 10
    else:
        print("please choose a level : hard or easy")
        return level()
# user choose a number
def guess():
    user_guess=int(input("make a guess:"))
    print(f"you choose {user_guess}")
    return user_guess

print("Welcome to the Number Guessing Game!")
print(logo)
number_of_attempts=level()
print("I've got a number between 1 and 100.")
answer = randint(1,100)

# check result
while number_of_attempts>0:
    user_guess= guess()
    if user_guess == answer :
            print("You win!")
            break
    elif user_guess > answer:
            print("too hight")
    elif user_guess< answer:
            print("too low")
    number_of_attempts-=1
print(f"game over, the answer is {answer}")