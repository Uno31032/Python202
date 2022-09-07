#import random
#random_integer = random.randint(1, 10)
#print(random_integer)
#..........4.1 Head or Tails............
#test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)
#random_side = random.randint(0,2)
#if random_side == 1:
#    print("Heads")
#elif random_side == 2:
#    print("Tail")
#else:
#    print("Big Mouse")
#................list.............
#tinh_thanh_vietnam = ["Hanoi","Bacgiang","Haiphong","Nghean"]
#print(tinh_thanh_vietnam[1])
#print(tinh_thanh_vietnam[-1])
#tinh_thanh_vietnam.append("Danang")#them vao list 1 piece o cuoi list
#print(tinh_thanh_vietnam)
#tinh_thanh_vietnam.extend(["Gialai","Daklak"])
#print(tinh_thanh_vietnam)
#.................4.2 Who is paying excercise..................
#namesAsCSV = input("Give me everybody's names ")
#names = namesAsCSV.split(",")

#num_items = len(names)
#random_choice = random.randint(0, num_items - 1)
#person_who_will_pay = names[random_choice]
#print(person_who_will_pay + " is going to buy the ticket")
#...........Treasure map excercise..............
#row1 = ["🥲","🥲","🥲"]
#row2 = ["🥲","🥲","🥲"]
#row3 = ["🥲","🥲","🥲"]
#map = [row1, row2, row3]
#print(f"{row1}\n{row2}\n{row3}")
#position = input("Where do you want to put the treasure? ")

#horizonal = int(position[0])
#vertical = int(position[1])

#selected_row = map[vertical-1]
#selected_row[horizonal-1] = "X"

#print(f"{row1}\n{row2}\n{row3}")
#........................final excercise...............................
import random
rock = ('''                                             
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                             
                                             
''')
paper = ('''                            
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              ''')
scissors = ('''  
   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
''')

game_image = [rock,paper,scissors]
user_choice = int(input("Choose a number 0.rock 1.paper 2.scissors: "))
print(game_image[user_choice])

random.seed(user_choice)
computer_choice = random.randint(0,2)
print("Computer choose: ")
print(game_image[computer_choice])

if user_choice >= 3 or user_choice <0:
    print("Your typed are invalid number,you lose!")
elif user_choice == 0 and computer_choice ==2:
    print("You win!")
elif user_choice == 2 and computer_choice ==0:
    print("You lose!")
elif computer_choice > user_choice :
    print("You lose!")
elif user_choice > computer_choice :
    print("You win!")
elif user_choice ==  computer_choice :
    print("It is a draw!")

