from flask import Flask, request, render_template_string
import hashlib

app = Flask(__name__)

# Simulated user credentials (username: user, password: secret)
USERNAME = "user"
PASSWORD_HASH = hashlib.sha256("hello".encode()).hexdigest()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        if username == USERNAME and password_hash == PASSWORD_HASH:
            return "Login successful!"
        else:
            return "Login failed!"

    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

