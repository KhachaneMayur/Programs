from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('details')),"<a href='/logout'>Logout</a>"


@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    session['user'] = POST_USERNAME
    session['pass'] = POST_PASSWORD
    if POST_USERNAME == 'admin' and POST_PASSWORD == 'password':
        return details()

@app.route('/details')
def details():
    if  session['user'] and  session['pass']:
        con = sql.connect('student.db')
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute('SELECT * FROM student')

        rows= cur.fetchall()
        return render_template('details.html',rows=rows)
    else:
        flash('You were successfully logged in')
        return redirect(url_for('index'))

@app.route("/logout")
def logout():
     session.pop('user',None)
     return home()


if __name__ == "__main__":
    app.run(debug=True)