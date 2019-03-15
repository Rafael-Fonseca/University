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

users_projects = {'rafael': [[0, 'ler documentação flask', '31/03/2019', 'Rafael'],
                             [1, 'ler documentação jinja', '31/03/2019', 'Rafael']],
                  'tonho': [[0, 'estudar IA', '31/03/2019', 'Tonho'],
                            [1, 'estudar paradigmas', '31/03/2019', 'Tonho']]}

projects_activities = {'rafael0':
[
    [0, 'Nome ativ_1 proj_0','14/03/2019', '31/03/2019', 'Rafael', 'Detalhamento Ativ 1'],
    [1, 'Nome ativ_2 proj_0','14/03/2019', '31/03/2019', 'Rafael', 'Detalhamento Ativ 2'],
    [2, 'Nome ativ_3 proj_0','14/03/2019', '31/03/2019', 'Rafael', 'Detalhamento Ativ 3']
],
                       'rafael1':
[
    [0, 'Nome ativ_1 proj_1','14/03/2019', '31/03/2019', 'Rafael', 'Detalhamento Ativ 1'],
    [1, 'Nome ativ_2 proj_1','14/03/2019', '31/03/2019', 'Rafael', 'Detalhamento Ativ 2'],
    [2, 'Nome ativ_3 proj_1','14/03/2019', '31/03/2019', 'Rafael', 'Detalhamento Ativ 3']
],
                       'tonho0':
[
    [0, 'Nome ativ_1 proj_0','14/03/2019', '31/03/2019', 'Tonho', 'Detalhamento Ativ 1'],
    [1, 'Nome ativ_2 proj_0','14/03/2019', '31/03/2019', 'Tonho', 'Detalhamento Ativ 2'],
    [2, 'Nome ativ_3 proj_0','14/03/2019', '31/03/2019', 'Tonho', 'Detalhamento Ativ 3']
],
                       'tonho1':
[
    [0, 'Nome ativ_1 proj_1','14/03/2019', '31/03/2019', 'Tonho', 'Detalhamento Ativ 1'],
    [1, 'Nome ativ_2 proj_1','14/03/2019', '31/03/2019', 'Tonho', 'Detalhamento Ativ 2'],
    [2, 'Nome ativ_3 proj_1','14/03/2019', '31/03/2019', 'Tonho', 'Detalhamento Ativ 3']
]}


# route to /
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']

        util = Utils()
        if util.validate_login(login, password):
            return render_template('oi.html', username=login, projects= users_projects)
        else:
            return render_template('index.html', erro='Login e/ou senha incorreto')

    return(render_template('index.html', erro='Método não permitido.'))


@app.route('/prepare_activities')
def prepare_activities():
    username = request.args.get('username')
    proj = request.args.get('proj')
    project_id = username+str(proj)

    return render_template('activities.html', username= username,
                    activities= projects_activities[project_id],
                           project= project_id)

@app.route('/activity')
def detail_activity():
    username = request.args.get('username')
    project_id = request.args.get('project_id')
    activity = request.args.get('activity')

    print(project_id, '\n', activity)
    my_activity = projects_activities[project_id][int(activity)]

    return render_template('activity.html', username= username,
                           activity= my_activity)

# Starting app
if __name__ == '__main__':
    app.run(debug=True)

