from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    # a = 1/0 I used this line to test argument debug of run function.
    return render_template('hello.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if True:  # valid_login(request.form['username'],
                  #     request.form['password']):
                  # Using form[key] we can cath a keyError if the user pass
                  # a key that does not exist in form, so is better use args
                  # attribute like in searchword = request.args.get('key', '')
                  # if you dont use get() be secure to cath the keyError
            return 'logado'  # log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


@app.route('/user/<username>')  # < put VARIABLES inside chevrons>
@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    '''
    url_for('name of the function of the route','parameters (if required)')
    Use this to refer a link to your url with variable in it
    and all other links because this prevents you from having to change the
    references to this url in your code
    
    Also serves to reference your static files
    url_for('static', filename='style.css')
    The file has to be stored on the filesystem as static/style.css
    '''


@app.route('/post/<int:post_id>')  # < Convert to this type : this variable >
def show_post(post_id):
    # Types that are accepted, string, int, float, path, uuid
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')  # Canonical page, if you request without trailing
# slash, the request will be accepted anyway.
def projects():
    return 'The project page'


@app.route('/about')  # Unique page, if you request without trailing slash
# you will obtain a 404 error like answer
def about():
    return 'The about page'


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')

'''
======================= F I L E -- U P L O A D ================================
To manipulate upload files make sure not to forget to set the 
enctype="multipart/form-data" attribute on your HTML form,
otherwise the browser will not transmit your files at all.

If you want to use the file name of the client to store the file on the server
use secure_filename() function, because, is more secure.
Ex: change the last line of upload_file() to
        f.save('/var/www/uploads/' + secure_filename(f.filename))
================== E N D -- F I L E -- U P L O A D ============================
'''

'''
============================= C O O K I E S ===================================
If you want to use sessions don't use cookies diretly, use Sessions, because it
add some security on top of cookies for you.
You can access cookies through cookies atribute of request, and you can set
cookies through set_cookie()

Ex: reading cookies
@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    

Ex: storing cookies
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
    
cookies are set on response objects, make_response make a response object
========================= E N D == C O O K I E S ==============================
'''

'''
=================== R E D I R E C T S  &  E R R O R S =========================
Use redirect() to redirect the use to another point
use abort() to abort a request early with an error code

You can customize error pages using errorhandler()

Ex:
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

The last 404, tells to flask that the status code of the page should be 404.
By default status code 200 is assumed.
=============== E N D == R E D I R E C T S  &  E R R O R S ====================
'''


'''
============================ S E S S I O N S ==================================
Sessions are objects which allows store information specific to a user from one
request to the next. This is implemented on top of cookies and sign the cookies
cryptographically, it means that the user could look your cookies but not
modify it, unless they know your secret key

Ex:

from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
    
    
 
======================= E N D == S E S S I O N S ==============================
'''

if __name__ == '__main__':
    app.run(debug=True)
