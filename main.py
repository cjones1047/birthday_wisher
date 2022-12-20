import pandas as pd
from glob import glob
import datetime
from random import choice
import smtplib
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.date(year=datetime.date.today().year,
                      month=11,
                      day=9)
birthday_df = pd.read_csv("birthdays.csv")
someones_birthday_row = birthday_df[(birthday_df["month"] == today.month) & (birthday_df["day"] == today.day)]
is_someones_birthday = bool(someones_birthday_row.size)
if is_someones_birthday:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
    # actual name from birthdays.csv
    all_letter_templates = [file_path for file_path in glob("./letter_templates/*")]
    chosen_template = choice(all_letter_templates)
    with open(chosen_template, "r") as template:
        template_text = template.read()
        birthday_name = someones_birthday_row["name"].item()
        letter_to_send = template_text.replace("[NAME]", birthday_name)
        print(letter_to_send)
    my_email = "100days1047@gmail.com"
    password = "cwlivsquszphscpw"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=someones_birthday_row["email"].item(),
                            msg=f"Subject:Happy Birthday\n\n"
                                f"{letter_to_send}")

# 4. Send the letter generated in step 3 to that person's email address.
