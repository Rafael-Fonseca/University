# Importing libs
from flask import Flask, url_for, redirect, request, render_template


class Utils:

    def read_file(self, file_name):
        file = open(file_name, "r+")
        lines = file.readlines()
        file.close()

        return lines

    def load_users(self, list_users):
        dict_current_users = {}
        for user in list_users:
            dict_current_users.update({user.split("|")[0]: user.split("|")[1]})

        return dict_current_users

    def load_grades(self, grades, user):
        dict_current_grades = {}
        for grade in grades:
            dict_current_grades.update({grade.split('|')[0]: grade.split('|')[1:-1]})
        return dict_current_grades.get(user)

    def validate_login(self, username, password):
        try:
            current_users = self.read_file("keylogs.txt")
        except FileNotFoundError:
            current_users = []

        dict_current_users = self.load_users(current_users)

        try:
            return password == dict_current_users[username]
        except KeyError:
            return False


# app Flask instance
app = Flask(__name__)


# route to /
@app.route('/')
def home():
    return render_template('teste.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']

        util = Utils()
        if util.validate_login(login, password):
            return render_template('oi.html', username=login, grades=util.load_grades(util.read_file('userGrades.txt'),login))
        else:
            return render_template('index.html', erro='Login e/ou senha incorreto')

    return(render_template('index.html', erro='Método não permitido.'))


# Starting app
if __name__ == '__main__':
    app.run(debug=True)

