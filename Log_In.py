from flask import Flask, redirect, render_template, request, session, url_for
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def Auth():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('home')), "<a href='/logout'>Logout</a>"


@app.route('/login', methods=['POST'])
def do_admin_login():
    Auth()
    session['user'] = request.form['username']
    session['pass'] = request.form['password']
    if session['user'] == 'admin' and session['pass'] == 'admin':
        return home()
    else:
        return "Username & Password incorrect. <a href='/login'>Log In</a>"


@app.route('/home')
def home():
    Auth()
    try:
        if session['user'] and session['pass']:
            con = sql.connect('student.db')
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM student')
            rows = cur.fetchall()
            return render_template('details.html', rows=rows)
    except:
        return "You are not logged in <br><a href = '/login'></b>" + \
               "click here to log in</b></a>"

@app.route("/login")
def logout():
    Auth()
    session.pop('username', None)
    return Auth()


if __name__ == "__main__":
    app.run(debug=True)