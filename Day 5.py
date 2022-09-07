#fruits = ["Apple","Peach","Pear"]
#for fruit in fruits:
#    print(fruit)
#    print(fruit + "pie")
#...................Average height excercise.............................
#student_heights = input("Input a list of student heights ").split(" ")
#for n in range(0, len(student_heights)):
#    student_heights[n] = int(student_heights[n])
    #print(student_heights)

#total_height = 0
#for height in student_heights:
#    total_height += height
    #print(total_height)

#number_of_students = 0
#for student in student_heights:
#    number_of_students += 1
    #print(number_of_students)

#average_height = round(total_height / number_of_students)
#print(f"Average height is {average_height}")
#..................5.2 Highest Score........................
#student_scores = input("Input a list of student score: ").split(" ")
#for n in range(0,len(student_scores)):
#    student_scores[n] = int(student_scores[n])
    #print(student_scores)

#highest_score = 0
#for score in student_scores:
#    if score > highest_score:
#        highest_score = score
#print(f"Your highest is {score}")
#..............................................
#total = 0
#for number in range(1, 101):
#    total += number
#print(total)
#.........................5.3 adding evens excercise...........................
#total = 0
#for number in range(0,101,2):
#    total += number
#print(total)
#total2 = 0
#for number1 in range(1,101):
#    if number1 % 2 == 0:
#        total2 += number1
#print(total2)
#.......................5.4 fizz buzz excercise............................
#total = 0
#for number in range(1,101):
#    if number % 3 == 0 and number % 5 == 0:
#        print("fizzbuzz")
#    elif number % 3 == 0:
#        print("fizz")
#    elif number % 5 ==0:
#        print("buzz")
#    else:
#        print(number)
#.......................final excercise........................................
import random   
letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
           'm','n','o','p','q','r','s','t','u','v','w',
           'x','y','z','A','B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&',
           '(',')','*','+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password_number = int(nr_letters + nr_symbols + nr_numbers)

password = " "
for char in range(1, nr_letters + 1):
    password  += random.choice(letters)


for char in range(1, nr_symbols + 1): 
    password  += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password  += random.choice(numbers)


#print(password)
random.shuffle(password)
print(password)




