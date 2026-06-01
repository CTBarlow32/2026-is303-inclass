'''
Name
Menu
Ratings
Pricing
Location
Deals
Times/days open
Nurtition
Back-story
Contact info
Merch
catering
app/rewards
Careers
Social Media
'''

class Restaurant:
    def __init__ (self,name, app, capacity):
        self.name = name
        self.menu = []
        self.reviews = []
        self.prices = [] #probably part of menu
        self.contact = {}
        self.app = app #link to app
        self.capacity = capacity

    def __str__(self):
        return f"{self.name} - App: {self.app} \
- Capacity {self.capacity} \
Price Range:  {self.calculate_price_range()} \n \
{self.convert_menu_to_str()}"


#inputs: none
#processes: loop through menu items, find min and max
#output: String: Min-Max
    def calculate_price_range (self):
        min_price = 99999999
        max_price = 0
        for menu_item in self.menu:
            if menu_item.price < min_price:
                min_price = menu_item.price
            if menu_item.price > max_price:
                max_price = menu_item.price
        return f"{min_price} - {max_price}"


    def convert_menu_to_str (self):
        menu_str = ""
        for menu_item in self.menu:
            menu_str += f"{menu_item.name} | {menu_item.price}\n"
        return menu_str
    

class menu_item:
    def __init__ (self, name, price, category, calories, ingredients):
        self.name = name
        self.price = price
        self.category = category
        self.calories = calories
        self.ingredients = ingredients #is this a string or list?
    
    def __str__ (self):
        return f"{self.name} | Price: ${self.price} | Category: {self.category} | Calories: {self.calories} | Ingredients: {self.ingredients}"

restaurant_1 = Restaurant("Wing Stop", "wingstop.com/app", 4)
restaurant_2 = Restaurant("Blue Line Deli", "BYU Dining", 60)

item_1 = menu_item("Classic Wings", 4.99, "Entree", 400, "chicken")
item_2 = menu_item("Fries", 6.99, "Side", 300, "Milk")
item_3 = menu_item("Dip", 1.89, "Sauce", 100, "ranch")
item_4 = menu_item("Dr Pepper", 1.99, "Drink", 150, "Drink")

restaurant_1.menu.append(item_1)
restaurant_1.menu.append(item_2)
restaurant_2.menu.append(item_3)
restaurant_2.menu.append(item_4)

print(restaurant_1)
print(restaurant_2)



