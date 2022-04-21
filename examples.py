import smtplib
import random


my_email = "bigbirthdaybuddyboy@gmail.com"
password = "9Pythons"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()    # Built-in feature to secure email connections
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="bigbirthdaybuddyboy@yahoo.com", 
#                         msg="Subject: Birthday Time\n\nHey there big birthday buddy")
    

import datetime as dt

now = dt.datetime.now()
# print(now)
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# print(day_of_week) # Monday=0, Tuesday=1 ...

# date_of_birth = dt.datetime(year=1987, month=10, day=16, hour=23, minute=33)
# print(date_of_birth)



today = now.weekday()

if today == 3:
    with open("quotes.txt") as quotes:
        quote_list = quotes.readlines()
        quote = random.choice(quote_list)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, 
                            msg=f"Subject:Thursday Motivathon\n\n{quote}")