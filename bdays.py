##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib



my_email = "bigbirthdaybuddyboy@gmail.com"
password = "9Pythons"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.month, now.day)
print(today)

data = pandas.read_csv("birthdays.csv")
# bday_dict = {datarow["name"]:(datarow.month, datarow.day) for (index, datarow) in data.iterrows()}  
bday_dict = {(datarow.month, datarow.day): datarow for (index, datarow) in data.iterrows()}  
# print(bday_dict)

letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

if today in bday_dict:
    person = bday_dict[today]
    print(person["email"])
    letter = random.choice(letter_list)
    with open(letter, 'r') as file :
        letter_text = file.read().replace("[NAME]", person["name"])
        # letter_text = letter_text.replace("[NAME]", person["name"])
        print(letter_text)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=person["email"], 
                            msg=f"Subject: Someone's having a birthday and we both know who\n\n{letter_text}")
    
    
    
    
# for (name, bday) in bday_dict.items():
#     if bday == today:
#         print(name)
#         # print(email)
#         letter = random.choice(letter_list)
#         with open(letter, 'r') as file :
#             letter_text = file.read().replace("[NAME]", name)
#             # letter_text.replace("[NAME]", name)
#             print(letter_text)



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




