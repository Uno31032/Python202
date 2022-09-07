##simple function...........................
#def greet():
#    print("hello")
#    print("How do you do")
#    print("Isn't the weather nice today?")
#greet()
##..............Function that allows for input...........................
#def greet_with_name(name,address):
#    print(f"Hello {name}")
#    print(f"How do you do in {address}")

#greet_with_name(123,"bin")
##Function with keword arguments
#greet_with_name(address="VietNam", name="Bin")
##...................Day 8.1 Area Calc.....................
#import math

#def paint_calc(height,width, cover):
#    area = height*width
#    num_of_cans = math.ceil(area/cover)
#    print(f"You'll need {num_of_cans} cans of paint.")
    

#test_h = int(input("Height of wall: "))
#test_w =  int(input("Width of wall: "))
#coverage = 5
#paint_calc(height=test_h, width=test_w, cover=coverage)
##..................Day 8.2 Prime Number Checker............
#def prime_checker(number):
#    is_prime = True
#    for i in range(2,number):
#        if number % i ==0:
#            is_prime = False
#    if is_prime:
#        print("It's a prime number.")
#    else:
#        print("It's not a prime number.")

#n = int(input("Check this number: "))
#prime_checker(number=n)
##...................Ceaser-cipher.....................

def ceaser(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
  
from art import logo
print(logo)

alphabet = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o',
            'p','q','r','s','t','u','v','w','x','y','z',
            'a','b','c','d','e','f','g','h','i','k','l','m','n','o',
            'p','q','r','s','t','u','v','w','x','y','z']

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift % 26
    ceaser(start_text = text, shift_amount=shift, cipher_direction=direction)
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")
        
    


#def encrypt(plain_text, shift_amount):
#    cipher_text = ""
#    for letter in plain_text:
#        position = alphabet.index(letter)
#        new_position = position + shift_amount
#        new_letter = alphabet[new_position]
#        cipher_text += new_letter
#    print(f"The encoded text is {cipher_text}")

#def decrypt(cipher_text, shift_amount):
#    plain_text = ""
#    for letter in cipher_text:
#        position = alphabet.index(letter)
#        plain_text += alphabet[new_position]
#    print(f"The decode text is {plain_text}")

#if direction == "encode":
#    encrypt(plain_text=text,shift_amount=shift)
#elif direction == "decode":
#    decrypt(cipher_text=text,shift_amount=shift)



    


