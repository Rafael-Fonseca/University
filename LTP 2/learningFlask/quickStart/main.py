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


@app.route('/login', methods=['GET', 'POST'])  # methods is GET by default
def login():
    if request.method == 'POST':
        return login()  # function that do_the_login()
    else:
        return login()  # function that show_the_login_form()


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


if __name__ == '__main__':
    app.run(debug=True)
