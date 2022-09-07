#....................................................
#print("Welcome to the rollercoaster!")
#height = int(input("What í your height in cm? "))

#if height > 120:
 #   print("You can ride the rollercoaster!")
#else:
   # print("Sorry, you have to grow taller before you can ride.")
#.................3.1 Odd or Even..........................
#number = int(input("Which number do you want to choose? "))
#if number % 2 ==1:
   # print("This is Even number!!!")
#else:
   # print("This is Odd number!!!")
#..................3.2 BMI Calculator 2.0................
#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))

#bmi = weight/height**2
#bmi_final = round(bmi,2)
#if bmi < 18.5:
    #print(f"Your bmi is {bmi_final},Underweight")
#elif 18.5<= bmi<25:
    #print(f"Your bmi is {bmi_final},Normal weight")
#elif 25<= bmi<30:
    #print(f"Your bmi is {bmi_final},Over weight")
#elif 30<= bmi<35:
    #print(f"Your bmi is {bmi_final},Obese")
#else:
   #print(f"Your bmi is {bmi_final},Clinically obese")
#3.3................ Leap year Excercise..................
#year = int(input("Which year do you want to check? "))
#if year % 4 ==0:
 #   if year % 100 == 0:
  #      if year % 400 == 0:
  #          print("Leap year.")
 #       else:
 #           print(("Not Leap year."))
 #   else:
 #       print("Leap year")
#else:
   # print("Not Leap year.")
#....................Ticket play game.....................
#height = int(input("Your height is: "))
#bill = 0
#if height >=120:
    #print("You can ride the rollercoaster!")
    #age = int(input("What is your age? "))
    #if age < 12:
    #    bill = 5
    #    print("Child ticket are $5.")
    #elif age<=18:
    #    bill = 7
    #    print("Youth ticket are $7.")
    #elif 45<= age <=55:
    #    print("Everything is going tobe OK.Have a free ride on us!")
    #else:
    #    bill = 12
    #    print("Adult tickets are $12.")

    #wants_photo = input("Do you want a photo taken? Y or N.")
    #if wants_photo =="Y" :
    #    bill +=3
    #    print(f"Your bill is {bill}$.")
    #elif wants_photo =="y":
    #    bill +=3
    #    print(f"Your bill is {bill}$.")
    #else:
    #    print(f"Your bill is {bill}$.")
#else:
    #print("Sorry, you have to grow taller before you can ride.")
#...........................Pizza order practice..........................
#money = 0
#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M, or L: ")
#add_pepperoni = input("Do you want pepperoni? Y or N: ")
#extra_cheese = input("Do you want extra cheese? Y or N: ") 
#if size == "S":
#    money += 15
#elif size == "M":
#    money += 20
#else:
#    money += 25
#if add_pepperoni == "Y":
#    if size == "S":
#        money += 2
#    else:
#        money += 3
#if extra_cheese == "Y":
#    money +=1
#print(f"Your final bill is {money} $")
#...........................if else condition ..........................
#...........................3.5 Love Caculator Excercise.....................
#print("Welcome to the Love Caculator!")
#name1 = input("What is your name?\n ")
#name2 = input("What is their name?\n ")

#combine_string = name1 + name2
#lower_case_name = combine_string.lower()
#b = lower_case_name.count("t")
#c = lower_case_name.count("r")
#d = lower_case_name.count("u")
#e = lower_case_name.count("e")

#first = b+c+d+e 

#f = lower_case_name.count("l")
#g = lower_case_name.count("o")
#h = lower_case_name.count("v")
#i = lower_case_name.count("e")

#second = f+g+h+i
#love_score = int(str(first)+str(second))

#if (love_score < 10) or (love_score > 90):
#    print(f"your score is {love_score}, you go together like coke and mentos")
#elif 40<= love_score<=50:
#    print(f"your score is {love_score}, you are alright together")
#else:
#    print(f"your score is {love_score}, you must keep trying!!!")
#....................final excercise............................
print("Welcome to treasure Island. Your mission is to find the treasure.")
first = input("Left or Right?\n").lower()


if first == "left":
    second = input("Swim or Wait?\n").lower()
    if second == "wait":
        third = input("Which door? Red, Blue, Yellow\n").lower()
        if third == "yellow":
            print("You Win!!!")
            print('''

  
     888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888  
                                                             
                    ''')
        elif third == "red":
            print("Game Over!!!!!")
        elif third == "blue":
            print("Game Over!!!!!")
        else:
            print("This question doesn't in answer. Game Over!!!")
    else:
        print("Game Over!!!!!")
else:
    print("Game Over!!!!!")

