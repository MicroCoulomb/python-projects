import smtplib
import datetime as dt
import pandas as pd

my_email = "naomiarchieves2@gmail.com"
my_pw = "eukw zudt zlly mglg"

bday_data = pd.read_csv('birthdays.csv')
bday_dict = bday_data.to_dict(orient='records')
print(bday_dict)

now = dt.datetime.now()
print(f"{now.month}-{now.day}")
for item in bday_dict:
    if item["month"] == now.month and item["day"] == now.day:
        with open("greetings_template.txt", "r") as f:
            greetings = f.read()
            greetings = greetings.replace("[NAME]", item["name"])
            print(greetings)
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_pw)
            connection.sendmail(from_addr=my_email, to_addrs=item["email"], msg="Subject:HAPPY BIRTHDAY\n\n" + greetings)
