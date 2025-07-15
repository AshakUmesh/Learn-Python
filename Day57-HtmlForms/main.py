from flask import Flask, render_template, request
import smtplib
import dotenv
import os
dotenv.load_dotenv("key.env")
app = Flask(__name__)

my_email=os.getenv("EMAIL")
password=os.getenv("PASSWORD")

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        sent_mail(name,email,phone,message)
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)


def sent_mail(name,email,phone,message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        email_message = f"Subject:You have a new Message\n\n Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=my_email,
            msg=email_message.encode("utf-8")
        )

if __name__ == "__main__":
    app.run(debug=True)
