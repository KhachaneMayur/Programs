from flask import Flask, redirect, render_template, request, session, url_for
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/')
def auth():
    if not session.get('logged_in'):
        return redirect(url_for('login_page'))
    else:
        return redirect(url_for('details'))

@app.route('/login_page')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    session['logged_in'] = True
    session['user'] = request.form['username']
    session['pass'] = request.form['password']
    if session['user'] == 'admin' and session['pass'] == 'admin':
        return redirect(url_for('details'))
    else:
        return "Username & Password incorrect. <a href='/login_page'>Log In</a>"



@app.route('/details')
def details():
    auth()
    con = sql.connect('student.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM student')
    rows = cur.fetchall()
    return render_template('details.html', rows=rows)


@app.route("/logout")
def logout():
    session.clear()
    return auth()


if __name__ == "__main__":
    app.run(debug=True)