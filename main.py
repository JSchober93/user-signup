from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/signup", methods=['post','get'])
def submit():
    username = request.form['username']
    password = request.form['password']
    verify_pass = request.form['verify_pass']
    email = request.form['email']
    
    user_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    #Username validation
    if username == "":
        user_error = "Username was left blank"
    elif len(username) < 3 or len(username) > 20:
        user_error = "Username is invalid - length allowed 3-20 characters"
        username = ""
    elif " " in username:
        user_error = "Username is invalid - contains a space"
        username = ""

    #Password validation
    if password == "":
        password_error = "Password was left blank"
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password is invalid - length allowed 3-20 characters"
        password = ""
    elif " " in password:
        password_error = "Password is invalid - contains a space"
        password = ""

    #Verify Password validation
    if verify_pass == "":
        verify_error = "Verify Password was left blank"
    elif len(verify_pass) < 3 or len(verify_pass) > 20:
        verify_error = "Verify Password is invalid - length allowed 3-20 characters"
        verify_pass = ""
    elif " " in verify_pass:
        verify_error = "Verify Password is invalid - contains a space"
        verify_pass = ""

    #Password/Verify match validation
    if password != verify_pass:
        password_error = "Password values don't match"
        password = ""
        verify_pass = ""

    #Email validation
    if email != "":
        if " " in email:
            email_error = "Email is invalid - contains a space"
            email = ""
        elif len(email) < 3 or len(email) > 20:
            email_error = "Email is invalid - length allowed 3-20 characters"
            email = ""
        elif email.count(".") < 1:
            email_error = "Email is invalid - does not contain a '.'"
            email = ""
        elif email.count(".") > 1:
            email_error = "Email is invalid - contains too many '.'"
            email = ""
        elif email.count("@") < 1:
            email_error = "Email is invalid - does not contain '@'"
            email = ""
        elif email.count("@") > 1:
            email_error = "Email is invalid - contains too many '@'"
            email = ""

    if not user_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template("signup.html", username=username, email=email, user_error=user_error, password_error=password_error, 
        verify_error=verify_error, email_error=email_error)


@app.route("/")
def index():
    return render_template('signup.html')


app.run()