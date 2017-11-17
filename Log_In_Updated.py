from flask import Flask, redirect, render_template, request, session, url_for
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/')
def Auth():
    if not session.get('logged_in'):
        return redirect(url_for('page'))
    else:
        return redirect(url_for('home')),"<a href='/logout'>Logout</a>"

@app.route('/page')
def page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    session['logged_in'] = True
    session['user'] = request.form['username']
    session['pass'] = request.form['password']
    if session['user'] == 'admin' and session['pass'] == 'admin':
        return home()
    else:
        return "Username & Password incorrect. <a href='/login'>Log In</a>"



@app.route('/home')
def home():
    Auth()
    con = sql.connect('student.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM student')
    rows = cur.fetchall()
    return render_template('details.html', rows=rows)

@app.route("/login")
def logout():
    session['logged_in'] = False
    return Auth()


if __name__ == "__main__":
    app.run(debug=True)