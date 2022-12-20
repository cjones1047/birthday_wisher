import pandas as pd
from glob import glob
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthday_df = pd.read_csv("birthdays.csv")
someones_birthday_row = birthday_df[(birthday_df["month"] == 5) & (birthday_df["day"] == 23)]
is_someones_birthday = bool(someones_birthday_row.size)
# birthday_month = someones_birthday_row["month"].item()
# birthday_day = someones_birthday_row["day"].item()
# print(f"{birthday_month} {birthday_day}")
print(f"Is someone's birthday?\n{is_someones_birthday}")
all_letter_templates = [file_path for file_path in glob("./letter_templates/*")]
print(all_letter_templates)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
# actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
