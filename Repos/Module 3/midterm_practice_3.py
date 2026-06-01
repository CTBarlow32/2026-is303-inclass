'''1:
Write a program that helps plan a party by calculating costs. The program should:
1. Ask the user for:
• Number of guests (a whole number)
• Cost per person for food (a number)
• Cost per person for drinks (a number)
• Whether they need to rent a venue: yes or no (a string)
2. Calculate:
• Food total (guests × food cost per person)
• Drink total (guests × drink cost per person)
• Venue cost: $0 if they do not need a venue, $250.00 if they do
• Grand total (food + drinks + venue)
3. Print a formatted summary using f-strings with costs formatted to 2 decimal places:
4. If grand total exceeds $500 print: "Tip: Ask guests to bring a dish to reduce costs!
'''


''' Number 2!!!
A personal trainer needs a weekly workout summary. Write a program that:
1. Ask the user how many workouts to log (a number)
2. For each workout, ask for:
• Activity name (a string) — e.g., Running, Swimming, Yoga
• Duration in minutes (a number)
• Whether it was outdoors: yes or no (a string)
3. Store each workout as a dictionary in a list. Each dictionary should have keys: "activity",
"minutes", and "outdoor" (True or False)
4. After all workouts are entered, calculate and display:
Total minutes (sum of all workout durations). Use the accumulator pattern.
Longest workout (the activity name and duration of the longest single workout). Use
the min/max pattern. If no workouts were entered, print "No workouts logged."
Outdoor workouts (a list of activity names that were done outdoors). Use the filter
pattern. If none were outdoors, print "No outdoor workouts this week."
'''
'''
num_of_workouts = int(input("How many workouts would you like to log: "))
workouts = []

for i in range(num_of_workouts):
    activity = input(f"Workout {i+1}. Activity: ").lower().strip()
    minutes = float(input(f"Workout {i+1}. Duration of Workout in minutes: "))
    outdoors = input(f"Was activity {i+1}. outside (yes/no): ").lower().strip()

    workouts.append({
        "activity": activity,
        "minutes": minutes,
        "outdoors": outdoors == "yes"
    })

#total minutes
total_minutes = 0
for w in workouts:
    total_minutes += w["minutes"]

#longest workout
longest = None
for w in workouts:
    if longest is None or w["minutes"] > longest["minutes"]:
        longest = w

#outdoors or not
outdoor_list = []
for w in workouts:
    if w["outdoors"]:
           outdoor_list.append(w["activity"])

#outputs
print("---Weekly Workout Summary---")
print(f"Total Minutes: {total_minutes}")
if longest:
     print(f"Your longest workout was {longest["activity"]} ({longest["minutes"]}) ")
else:
     print("No workouts this week bum")

if len(outdoors) > 0:
       print(f"Outdoor Workouts: {','.join(outdoor_list)}")
else:
     print("No outdoor workouts")
'''

''' #3 problem
A group of friends is planning movie night and needs to organize votes. Write a program that:
1. Ask for the name of the person hosting (a string)
2. Use a while loop to let the user add movie votes one at a time. After each vote, ask
"Add another vote? (yes/no)". Stop when the user types "no".
3. For each vote, collect:
• Voter name (a string)
• Movie title (a string)
• Genre: "action", "comedy", "horror", or "drama" (a string)
4. Clean each votes data before storing:
• Voter name should be converted to title case (e.g., "jane doe" → "Jane Doe")
• Movie title should be converted to title case
• Genre should be converted to lowercase and stripped of whitespace
5. Store each vote as a dictionary in a list with keys: "voter", "movie", "genre"
6. After voting closes, produce a report:
• Total number of votes
• Number of comedy votes and number of non-comedy votes (use an accumulator or
counter)
• A numbered list of all votes showing voter, movie, and genre (use a for loop with the
index)
• If more than half the votes are for comedy, print: "Looks like a comedy night!"
'''

host = input("Name of Host: ").title().strip()

votes = []
keep_going = "yes"


while keep_going == "yes":
    voter = input("Name of Voter: ").strip().title()
    movie = input("Name of Movie: ").strip().title()
    genre = input("Movie Genre: ").strip().lower()

    votes.append({
        "voter": voter,
        "movie": movie,
        "genre": genre
    })

    keep_going = input("Do you want to add another voter (yes/no): ").strip().lower()

#accumulator
comedy_count = 0
other_count = 0
for vote in votes:
    if vote['genre'] == "comedy":
        comedy_count += 1
    else:
        other_count += 1
total_vote = comedy_count + other_count
#output
print(f"---Movie Night Report (hosted by {host})---")
print(f"Total Votes: {total_vote}")
print(f"Comedy Votes: {comedy_count}")
print(f"Other Votes: {other_count}")
print("All Votes: ")
for i in range(len(votes)):
    v = votes [i]
    print(f"{i+1}. {v['voter']} picked {v['movie']} ({v['genre']})")
if comedy_count > total_vote/2:
    print("Looks like its a comedy night")