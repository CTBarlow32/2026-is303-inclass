
from enum import member


MEMBERS = {
    "M001": {"name": "Sarah Johnson",  "discount": 0.10},
    "M002": {"name": "Mike Chen",      "discount": 0.15},
    "M003": {"name": "Emma Davis",     "discount": 0.05},
}

#do you have a discount?
member_id = input("Do you have member discount? (yes/no) ").lower()

#if yes
if member_id == "yes":
    id = input("What is your member ID: ").capitalize()
    if id in MEMBERS.keys():
        member = MEMBERS[id]
        print(f" Hi {member['name']}, your discount is {member['discount']} ")

'''total_discount = total_cost * {member[discount]:.2f}'''

#if no
    else:
        print("Total is ...  ")
    