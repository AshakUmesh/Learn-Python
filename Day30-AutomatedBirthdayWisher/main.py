import random
import smtplib
import datetime
import pandas


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (row["month"], row["day"]): row
    for _, row in data.iterrows()
}
email = "ashakumesh2020@gmail.com"
password = "gzlxuwyvhpqkgvyq"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=email,password=password)


now = datetime.datetime.now()
month = now.month
day = now.day

if (month , day) in birthdays_dict:
    person = birthdays_dict[(month, day)]
    send_email = person["email"]
    send_name = person["name"]
    with open("letter_templates/letter_3.txt",encoding="utf-8") as file:
        letter = file.read()
    new_letter = letter.replace("[NAME]", send_name)
    send_message = "Subject: Happy Birthday \n\n" + new_letter
    connection.sendmail(from_addr=email , to_addrs=send_gmail,msg=send_message.encode("utf-8"))