'''
Carter Barlow - IS 303 A01

Data Analytics
I am making a survey analyzer that calculates the average number of surveys per
topic based on the number of respondents and the total ratings. 

Inputs:
-Survey topic (string)
-Number of respondents (integer)
-Total of all ratings (integer)

Processes:
-Total of all ratings / # of respondents

Outputs:
-Average rating for the survey topic
'''

#Inputs:
survey_topic = input("Enter Survey Topic: ")
num_respondents = int(input("Enter Number of Respondents: "))
total_ratings = int(input("Enter Total number of Ratings: "))

#Processes:
average_rating = total_ratings / num_respondents

#Outputs:
print(f"The average rating of {survey_topic} is {average_rating:.2f}.")