'''
1. Ask the user how many sales to enter (a number)

2. For each sale, ask for:
   - Item name (a string)
   - Sale amount in dollars (a number)
   - Whether it was a return: yes or no (a string)

3. Store each sale as a dictionary in a list. Each dictionary should have keys: `"item"`, `"amount"`, and `"is_return"` (True or False)

4. After all sales are entered, calculate and display:
   - Total revenue (sum of all non-return amounts, minus return amounts). Returns should be subtracted, not added. Use the accumulator pattern.
   - Largest sale (the item name and amount of the highest non-return sale). Use the min/max pattern. If there are no non-return sales, print "No sales recorded."
   - Returns list (the names of all items that were returns). Use the filter pattern. If there are no returns, print "No returns today."

5. Print a formatted summary:
   --- Daily Sales Report ---
   Total revenue: $247.50
   Largest sale: Winter Jacket ($89.99)
   Returns: Broken Lamp, Wrong Size Shirt

Constraints:
- You must use a `for` loop to process the list
- You must store data in a list of dictionaries
- You must use at least two named loop patterns (accumulator, min/max, or filter)
'''

num_of_sales = int(input("How many sales will you be entering: "))

sales = []

for i in range(num_of_sales):
    item = input("Item Name: ").lower().strip()
    amount = float(input("Sale amount in dollars: "))
    is_return = input("Was it a return (yes/no): ").lower().strip()

    sales.append({
        "item": item,
        "amount": amount,
        "is_return": is_return == "yes"
    })

#total sum
w = []
total = 0
positive = 0
negative = 0
for w in sales:
    if is_return == "true":
        negative += w['amount']
    else:
        positive += w['amount']
total = positive - negative

#largest sale len...
largest = None
for w in sales:
    if largest is None or w['amount'] > largest['amount'] and w['is_return'] is not "yes":
        largest = w

#output
print("--- Daily Sales Report---")
print(f"Total Revenue: ${total:.2f}")
if largest:
    print(f"Largest Sale: {w['item']} (${w['amount']:.2f})")
else:
    print("No Sales Recorded")

if is_return == "yes":
    print(f"Returns: {','.join['is_return']}")

