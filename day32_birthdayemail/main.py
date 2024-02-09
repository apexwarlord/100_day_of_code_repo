import datetime as dt
import pandas
import smtplib
import random
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = "alexzacharias01@hotmail.com"
PASSWORD = os.getenv("PASSWORD")
LETTER_PATHS = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]


def send_letter(bday_dict):
    letter_path = random.choice(LETTER_PATHS)
    with open(letter_path, "r") as letter_file:
        letter = letter_file.read().replace("[NAME]", bday_dict["name"])

    with smtplib.SMTP('smtp.office365.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=f"{bday_dict['email']}",
            msg=f"Subject:HAPPY BIRTHDAY {bday_dict['name']}!\n\n{letter}"
        )


birthday_db = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_db.to_dict(orient="records")

today = dt.datetime.today()

for birthday in birthday_dict:
    if birthday["month"] == today.month and birthday["day"] == today.day:
        send_letter(birthday)

# if today.weekday() != 0:
#     sys.exit("Not monday")

# with open("quotes.txt", "r") as f:
#     quotes = [quote.rstrip() for quote in f.readlines()]
#
# with smtplib.SMTP('smtp.office365.com') as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs="alexzacharias01@gmail.com",
#         msg=f"Subject:Inspirational Monday!\n\n{random.choice(quotes)}"
#     )
#


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
