from flask import Flask, request, redirect

app = Flask(__name__)

'''
@app.route('/')
def calculator():
    return '<form action="/redirecti">' \
           '<input name=n1><br>' \
           '<input name=n2><br>' \
           '<input type="radio" name="option" value="somar">Somar<br>' \
           '<input type="radio" name="option" value="subtrair">Subtrair<br>' \
           '<input type="radio" name="option" value="multiplicar">Multiplicar<br>' \
           '<input type="radio" name="option" value="dividir">Dividir<br>' \
           '<input type="submit" value="Enviar">' \
           '</form>'
'''


@app.route('/')
def calculator():
    return '<form action="/somar">' \
           '<input name="n1"><br>' \
           '<input name="n2"><br>' \
           '<input type="submit" value="Somar">' \
           '<input type="submit" formaction="/subtrair" value="Subtrair">' \
           '<input type="submit" formaction="/multiplicar" value="Multiplicar">' \
           '<input type="submit" formaction="/dividir" value="Dividir">' \
           '</form>'

@app.route('/somar')
def soma():
    return str(int(request.args.get('n1', default='0')) + int(request.args.get('n2', default='0')))


@app.route('/subtrair')
def sub():
    return str(int(request.args.get('n1', default='0')) - int(request.args.get('n2', default='0')))


@app.route('/multiplicar')
def mul():
    return str(int(request.args.get('n1', default='0')) * int(request.args.get('n2', default='0')))


@app.route('/dividir')
def div():
    return str(int(request.args.get('n1', default='0')) / int(request.args.get('n2', default='1')))

'''
@app.route('/redirecti')
def redirecti():
    url = '/' + request.args.get('option') +'?n1=' + request.args.get('n1') +'&n2='+ request.args.get('n2')
    return redirect(url)
'''
app.run(debug=True)