logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
'+': add, 
'-': subtract,
'*': multiply,
'/': divide,
}

def calculator():
  print(logo)

  num1 = float(input("What is the first number?: "))
  run = True
  while run: 
    for e in operations:
      print(e)
    perform = input("Type a math operation: ") 
    num2 = float(input("What is the next number?: "))

    calculation = operations[perform]
    answer = calculation(num1, num2)

    print(f"{num1} {perform} {num2} = {answer}")
    print(f"Type 'y' to continue calculating with {answer}, type 'n' to exit or type 'new' for a brand new calculation")
    continue_calc = input("Type yes/no/new: ")
    if continue_calc == 'yes':
      run = True
      num1 = answer
    elif continue_calc == 'no':
      run = False
      print("\n End.")
    elif continue_calc == 'new':
      calculator()
    else:
      print("Invalid response.")
      run = False
      print("\n End.")
hi=calculator()
