##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt


# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

print(data.year)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

with open("birthdays.csv") as bday_data:
    

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




