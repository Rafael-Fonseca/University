# Importing libs
from flask import Flask, url_for, redirect, request, render_template

# app Flask instance
app = Flask(__name__)


# route to /
@app.route('/')
def home():
    return redirect(url_for('static', filename='index.html'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']

        if login == 'r' and password == '3':
            return render_template('oi.html', username=login)

    return(redirect(url_for('static', filename='index.html')))

# Starting app
if __name__ == '__main__':
    app.run(debug=True)
