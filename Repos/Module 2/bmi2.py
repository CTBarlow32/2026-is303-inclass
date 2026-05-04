'''
Inputs: 
- Name
- Height
- Weight
- Age
- Sex

Processes:
- Input Validation
- Caculate BMI - weight/height^2 * 703
- Categorize BMI
    - Underweight < 18.5
    - Normal weight 18.5 - 24.9
    - Overweight 25 - 29.9
    - Obese 30 or higher

Outputs:
- Report for Individual
'''

#input
name = input("Name: ")
age = input ("Age: ")
sex = input("Sex: ")
height = input("Height (inches) : ")
weight = input("Weight (pounds) : ")

#Input Validation
age = age.replace(".","",1)
age_is_int = age.isdigit()
if age_is_int == True:
    age = int(age)
age_is_reasonable = True
if age_is_int == True and age > 140 or age < 1:
    age_is_reasonable = True

sex = sex.lower()
sex_is_valid = True
if sex == "Male" or sex == "Female":
    sex_is_valid = True

height = height.replace(".","",1)
height_is_int = height.isdigit()
if height_is_int == True:
    height = int(height)
height_is_reasonable = True
if height_is_int == True and (height <12 or height <= 140):
    height_is_reasonable = True

weight = weight.replace(".","",1)
weight_is_int = weight.isdigit()
if weight_is_int == True:
    weight = int(weight)
weight_is_reasonable = True
if weight_is_int == True and (weight <12 or weight <= 1200):
    weight_is_reasonable = True

    ready_to_process = True

    if age_is_int == False or age_is_reasonable == False:
        print("You entered invalid age, please use whole numbers")
        ready_to_process = False

    if sex_is_valid == False:
        print("You entered unexpected sex, please use male/female")
        ready_to_process = False

    if height_is_int == False or height_is_reasonable == False:
        print("Please use whole numbers between 1 and 140 in inches")
        ready_to_process = False

    if weight_is_int == False or weight_is_reasonable == False:
        print("Please use whole numbers between 12 and 1200 pounds")
        ready_to_process = False

    if weight_is_int == False or weight_is_reasonable == False:
        print("Please use whole numbers between 12 and 1200 pounds")
        ready_to_process = False

'''
- Caculate BMI - weight/height^2 * 703
- Categorize BMI
    - Underweight < 18.5
    - Normal weight 18.5 - 24.9
    - Overweight 25 - 29.9
    - Obese 30 or higher
'''

if ready_to_process == True:
    bmi = (weight / height**2) *703
    bmi_category = ""
    if bmi < 18.5:
        bmi_category = "underweight"
    elif bmi <= 24.9:
        bmi_category = "healthy"
    elif bmi <= 29.9:
        bmi_category = "overweight"
    elif bmi <= 39.9:
        bmi_category = "obese"
    else: 
        bmi_category = "extremely obese"

#report
    print(f"Report for {name}\n"
          f"{age} year old {sex}\n"
          f"Your BMI is {bmi}\n"
          f"Your BMI category is: {bmi_category}")



