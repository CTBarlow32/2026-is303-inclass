'''

Inputs:
- age
-day of week
-height
-VIP
-Signed Waiver
-parent present

Proccesses:
-Use variables to identify which rides are available/

Outputs:
-List of rides

'''

#inputs
age = int(input("Age: "))
day_of_week = input("Day of Week: ").lower()
height = int(input("Height in inches: "))
vip = input("VIP? yes/no ").lower()
signed_waiver = input("Signed Waiver? yes/no ").lower()
parent_present = input("Parent Present? yes/no ").lower()

#megadrop

ride_found = False

if age >=14 and signed_waiver == "yes":
    if height >= 54:
        #print("Megadrop")
        ride_found = True
    elif vip == "yes" and height >= 50:
        print("Megadrop")
        ride_found = True

#thunderbolt
if age >= 10 and height >= 48 and day_of_week != "monday":
    print("Thunderbolt")
    ride_found = True

#Kiddie
if age > 8 or parent_present == "yes":
    print("Kiddie")
    ride_found = True

if not ride_found:
    print("No rides available.")

