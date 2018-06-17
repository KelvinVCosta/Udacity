from flask import Flask, redirect, url_for, render_template, request, jsonify, session
app = Flask(__name__)
app.config['SECRET_KEY']='thisisasecretkey'


@app.route('/')
def home():
    if 'user' in session:
        return render_template('message.html', username=session['user'])
    return redirect(url_for('login_func'))


@app.route('/login', methods=['GET', 'POST'])
def login_func():
    if request.method == "GET":
        message = 'Hey there'
        return render_template('login.html', message=message)

    username = request.form['username']
    password = request.form['password']
    print("username is {} and password is {}".format(username, password))
    session['user'] = username
    return render_template('message.html', username=session['user'])


@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('logout.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
