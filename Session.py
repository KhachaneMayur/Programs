from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
import sqlite3 as sql

engine = create_engine('sqlite:///tutorial.db', echo=True)

app = Flask(__name__)


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
    # if :
    #     session.get['logged_in'] = True
    # else:
    #     flash('wrong password!')
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
        return redirect(url_for('/index'))

@app.route('/index')
def index():
   if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"
@app.route("/logout")
def logout():
     session.pop('user')
     return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=5000)