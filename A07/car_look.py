import requests

def get_fuel_data(year,make,model):
    '''
    Inputs:
        year int
        make string
        model string
    Processes:
        look up vehicle id using fueleconomy.gov
        use vehicle id to get comb08 mpg
    
    output:
        combined mpg
    notes: 

    https://www.fueleconomy.gov/ws/rest/vehicle/menu/options?year=2020&make=Honda&model=Civic%204Dr
    https://www.fueleconomy.gov/ws/rest/vehicle/42149    
    '''
    if year <1900 or year > 2100:
        print("Please enter reasonable year.")
        return 0


    base_url = "https://www.fueleconomy.gov/ws/rest/"
    base_headers = {"Accept":"application/json"}
    url = base_url + f"vehicle/menu/options?year={year}&make={make}&model={model}"
    response = requests.get(url, headers=base_headers)
    #print(response.text)
    data = response.json()
    if type (data["menuItem"]) == list:
        vehicle_id = data["menuItem"][0]["value"]
    else:
        vehicle_id = data["menuItem"][0]["value"]

#Second call to grab the MPG for the vehicle ID
    url = base_url + f"vehicle/{vehicle_id}"
    response = requests.get(url, headers=base_headers)
    data = response.json()
    print(data["comb08"])
    return data["comb08"]





from bs4 import BeautifulSoup
import time

"""
    inputs:
        make string
        models tring
    processes
        scrape data to get 10-year maintenance costs for the make and model
    output:
        use caredge.com
https://caredge.com/honda/civic/maintenance
"""


def get_maintenance_cost(make, model):
    base_url = "https://caredge.com/"
    base_headers = {"User-Agent": "Mozilla/5.0"}
    url = base_url + f"{make.lower()}/{model.lower()}/maintenance"
    response = requests.get(url, headers=base_headers)
    #print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find_all("table")[0]
    total_maintenance = 0
    for row in table.find_all("tr")[1:]:
        cells = [td.get_text(strip=True)for td in row.find_all("td")]
        dollar_amount = cells[2]
        dollar_amount = dollar_amount.replace("$","")
        dollar_amount = dollar_amount.replace(",","")
        int_amount = int(dollar_amount)
        total_maintenance +=int_amount
    return total_maintenance


list_of_vehicles = [
    {"year": 2020, "make": "Honda", "model": "Civic", "extra_text": " 4DR"},
    {"year":2020, "make": "Chevrolet", "model": "Blazer", "extra_text": " AWD"},
    {"year":2023, "make": "Toyota", "model": "Corolla", "extra_text": ""}
]

for vehicle in list_of_vehicles:
    mpg = get_fuel_data(vehicle["year"], vehicle["make"], vehicle["model"]+vehicle["extra_text"])
    ten_year_maintenance = get_maintenance_cost(vehicle["make"], vehicle["model"])
    tco = 11000*10/int(mpg)*4.50 + ten_year_maintenance
    print(f"{vehicle["year"]} {vehicle["make"]} {vehicle["model"]} TCO: {tco}")
    time.sleep(3)
