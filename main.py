import pandas
import random
import datetime as dt
import smtplib
from decouple import config

username = "beardwhite456@gmail.com"
password = config("PASS")
data = pandas.read_csv("birthdays.csv")
new_data = data.to_dict("records")
user_data = random.choice(new_data)
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

now = dt.datetime.now()
today = now.day
month = now.month
if today == 29 and month == 6:
    with smtplib.SMTP_SSL('smtp.gmail.com') as connection:
        connection.login(user=username, password=password)
        with open(f"./letter_templates/{random.choice(letters)}", "r") as file:
            current_file = file.read()
            new_letter = current_file.replace("[NAME]", user_data["name"])
        connection.sendmail(from_addr=username, to_addrs="livinglavidaloca29@gmail.com",
                            msg=f"Subject:HBD{user_data['name']}\n\n{new_letter}")