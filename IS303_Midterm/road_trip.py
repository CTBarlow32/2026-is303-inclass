'''
1. Ask the user for:
   - Total distance in miles (a number)
   - Vehicle fuel efficiency in miles per gallon (a number)
   - Current gas price per gallon (a number)
   - Whether they have a toll pass: yes or no (a string)

2. Calculate:
   - Gallons of gas needed (distance / fuel efficiency)
   - Gas cost (gallons * price per gallon)
   - Toll cost: $0 if they have a toll pass, $15.00 if they do not
   - Total trip cost (gas cost + toll cost)

3. Print a summary using f-strings with costs formatted to 2 decimal places:
   --- Trip Cost Summary ---
   Distance: 300 miles
   Gas needed: 10.00 gallons
   Gas cost: $35.00
   Toll cost: $15.00
   Total cost: $50.00

4. If the total cost exceeds $100, print: "Consider carpooling to split the cost!"

Constraints:
- You must use at least one `if`/`else` (for the toll pass check)
- You must use f-strings for all output
- Your program should handle both "yes" and "Yes" and "YES" (case-insensitive)
'''
#inputs
total_distance = float(input("Total distance in Miles: "))
gph = float(input("Vehicle fuel efficiency in miles per gallon: "))
current_gas_price = float(input("Current Gas Price per Gallon: "))
toll_pass = input("Do you have a toll pass (yes/no): ").lower().strip()

#processes
gallons_needed = total_distance / gph
gas_cost = current_gas_price * current_gas_price

toll_cost = 0
if toll_pass == "yes":
    toll_cost = 0
else:
    toll_cost = 15

total_cost = gas_cost + toll_cost

#outputs
print("---Total Cost Summary---")
print(f"Distance: {total_distance} miles")
print(f"Gas Needed: {gallons_needed:.2f} gallons")
print(f"Toll Cost: ${toll_cost:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

if total_cost > 100:
    print("Consider carpooling to split the cost!")