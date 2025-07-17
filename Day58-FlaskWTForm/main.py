from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Length(min=6, max=50)])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "hiiammisterchittyashak"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")


def login_access(email, password):
    user_email = "admin@email.com"
    user_password = "12345678"
    if user_email == email and user_password == password:
        return render_template("success.html")
    else:
        return render_template("denied.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data)
        return login_access(login_form.email.data, login_form.password.data)
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
