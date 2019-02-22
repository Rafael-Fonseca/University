from flask import Flask, request, url_for

#  Object Flask
app = Flask(__name__)


#  route to /
@app.route('/')
def home():
    return '<html>' \
           '<form action="/exibir">' \
           '<fieldset>' \
           '<input type="text" name="name"></input> <br>' \
           '<input type="text" name="lastname"></input> <br>' \
           '<input type="submit" value="Submit">' \
           '</form>'\
           '</html>'


#  route to /nome
@app.route('/nome')
@app.route('/name')
def name():
    dados = request.method
    return dados


@app.route('/exibir')
def show():

    return (request.args.get('name', default='Nome não informado') + ' '
            + request.args.get('lastname', default='Sobrenome não informado'))
    '''
    if request.args.get('name') == None:
        return 'Você não inseriu um nome.'
    return request.args.get('name')
    '''


#  start app
if __name__ == '__main__':
    app.run(debug=True)
