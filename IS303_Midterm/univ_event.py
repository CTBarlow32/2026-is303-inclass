'''
keep_going = "yes"
shiz...
while keep_going =="yes"
keep_going = Inpout"is it done"?
'''

'''
1. Ask for the event name (a string)
2. Use a while loop to let the user register attendees one at a time. After each registration, ask "Register another? (yes/no)". Stop when the user types "no".
3. For each attendee, collect:
   - Full name (a string)
   - Email address (a string)
   - Role: "member" or "guest" (a string)
4. Clean each attendee's data before storing:
   - Name should be converted to title case (e.g., "jane doe" becomes "Jane Doe")
   - Email should be converted to lowercase and have whitespace stripped
   - Role should be converted to lowercase
5. Store each attendee as a dictionary in a list with keys: "name", "email", "role"
6. After registration closes, produce a report:
   - Total number of attendees
   - Number of members and number of guests (use an accumulator or counter)
   - A list of all attendee names, numbered (use a for loop with the index)
   - If there are more guests than members, print: "Consider a membership drive!"

   Example output:
   --- Registration Report: Python Workshop ---
   Total attendees: 4
   Members: 1
   Guests: 3
   Attendee List:
   1. Alice Chen (member)
   2. Bob Smith (guest)
   3. Carol Jones (guest)
   4. David Lee (guest)

   Consider a membership drive!


Constraints:
- You must use a while loop for the registration process (not a for loop with a fixed count)
- You must use string methods to clean the data (title case, lowercase, strip)
- You must use a list of dictionaries to store attendees
- You must use at least one loop pattern (accumulator or counter) for the member/guest counts
- You must use a conditional for the membership drive message
'''

event_name = input("Name of Event: ")

keep_going = "yes"
registration = []

while keep_going == "yes":
    name = input("Enter Full Name: ").title()
    email = input("Enter Email Address: ").lower().strip()
    role = input("Enter Role (member/guest): ").lower()

    registration.append({
        "name": name,
        "email": email,
        "role": role
    })

    keep_going = input("Do you have another person to add: ")

#processes
total = 0
members = 0
guests = 0
for w in registration:
    if w['role'] == "member":
        members += 1
    else:
        guests += 1
total = members + guests

#output
print(f"---Registration Report: {event_name}")
print(f"Total attendees: {total}")
print(f"Members: {members}")
print(f"Guests: {guests}")
print("Attendee list:")
for w in registration:
    if w['role'] == 'member' or w['role'] == "guest" :
        print(f"{i+1}. {w['name']}, ({w['role']})")

