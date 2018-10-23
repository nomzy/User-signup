from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index ():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def signup_validation():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    username_error_msg =""
    password_error_msg =""
    verify_password_error_msg =""
    email_error_msg =""

    if len(username) < 3 or len(username) > 20 or " " in username:
        username_error_msg = "Invalid username"
        username = ""
    if len(password) < 3 or len(password) > 20 or " " in password:
        password_error_msg = "Invalid Password"
        password = "" 
    if password != verify_password or verify_password =="":
        verify_password_error_msg = "Password does not match"
        verify_password = ""
    if email != "" and len(email) < 3 or len(email) > 20:
        email_error_msg = "Incorrect email"
        email= ""

    elif email != "" and (" " not in email or "@" not in email or "." not in email):
        email_error_msg = "Incorrect email"
        email = ""

    if not username_error_msg and not password_error_msg and not verify_password_error_msg and not email_error_msg:
        return render_template('homepage.html', username = username)
    else:
        return render_template('index.html', username_error_msg = username_error_msg, password_error_msg = password_error_msg,verify_password_error_msg = verify_password_error_msg,email_error_msg = email_error_msg, username = username, email =email)

app.run ()
