#............9.1 Grading program.............................
# student_scores = {
#     "Harry":81,
#     "ROn": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
#     }
# student_grades = {}
# 
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student]= "Outstanding"
#     elif score >80:
#         student_grades[student]= "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student]="Acceptable"
#     else:
#         student_grades[student]="Fail"
# 
# print(student_grades)
#.....................
# travel_log = [
#     {"country":"France",
#      "total_visits":12,
#      "cities_visited": ["Paris","Lillie","Dijon"]},
#     {"country":"Germany",
#      "total_visits":5,
#      "cities_visited": ["Berlin","Hamburg","Stuttgart"]},
#     ]
# #................Dictionary in list Excercise............................
# 
# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)
#     
# add_new_country("Russia",2,["Moscow","Saint Petersburg"])
# print(travel_log)
##....................Final.................
import os
from turtle import clear
def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
bidding_finished = False
while not bidding_finished:
    bids = {}
    name = input("What is your name? ")
    price = int(input("What is your bid? "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or no'.")
    if should_continue =="no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('clear')
        


