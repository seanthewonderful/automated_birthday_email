##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.month, now.day)
print(today)

data = pandas.read_csv("birthdays.csv")
bday_dict = {datarow["name"]:(datarow.month, datarow.day) for (index, datarow) in data.iterrows()}  
# print(bday_dict)

letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

for (name, bday) in bday_dict.items():
    if bday == today:
        print(name)
        letter = random.choice(letter_list)
        with open(letter, 'r') as file :
            letter_text = file.read()
        letter_text = letter_text.replace("[NAME]", name)
        print(letter_text)



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




