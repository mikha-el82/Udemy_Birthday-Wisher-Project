##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import random
import pandas as pd
import os

data = pd.read_csv("birthdays.csv")
# print(data)

now = dt.datetime.now()
this_day = now.day
this_month = now.month

has_birthday_today = data[(data.month == this_month) & (data.day == this_day)].name.to_list()
# print(f"\nThe list is: *{has_birthday_today}*, the length is *{len(has_birthday_today)}*")

letter_templates = os.listdir("letter_templates")
# print(letter_templates)

for name in has_birthday_today:
    selected_template_name = random.choice(letter_templates)
    selected_template_path = f"letter_templates/{selected_template_name}"
    with open(selected_template_path) as letter:
        letter_content = letter.read()
        new_letter = letter_content.replace("[NAME]", "Michal")
        print(new_letter)
        print("------------------------")

        # send_to = data[(data.name == name)].email.to_str()
        #
        # sender = "Michal <michal@example.com>"
        # receiver = f"{name} <to@example.com>"
        #
        # message = f"""\
        #     Subject: Hi Mailtrap
        #     To: {receiver}
        #     From: {sender}
        #
        #     {quote}"""
        #
        # with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        #     server.starttls()
        #     server.login("e459c3f6880fcc", "26c63def9cd9c8")
        #     server.sendmail(sender, receiver, message)









