import datetime as dt
import smtplib
import pandas
import random


MY_EMAIL = "tinydemo@gmail.com"  # Your email here
MY_PASSWD = "qazplm@12345" # Your password here
FROM_NAME = "Your Name Here"     # You can customize this



today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter-{random.randint(1, 10)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])
        contents = contents.replace("[FROM]", FROM_NAME)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )



