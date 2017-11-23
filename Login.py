from flask import Flask, redirect, render_template, request, session, url_for, json
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'random string'


def auth():
    if session.get('user') != 'admin' and session.get('pass') != 'admin':
        return redirect(url_for('login_page'))
    return True


@app.route('/login_page')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    session['user'] = request.form['username']
    session['pass'] = request.form['password']
    if session['user'] == 'admin' and session['pass'] == 'admin':
        return redirect(url_for('details'))
    return redirect(url_for('login_page'))
    #con = sql.connect('admin.db')
    #cur = con.cursor()
    #if cur.execute('SELECT * FROM admin WHERE username= ? and password = ?',(session['user'],session['pass'])):
    #    return details()
    #return login_page()

@app.route('/info/<rollno>', methods=['GET'])
def info(rollno):
    con = sql.connect('student.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('''SELECT * FROM student WHERE RollNo= ?''', (rollno,))
    rows = cur.fetchall()
    return render_template('details.html', rows=rows)


@app.route('/details')
def details():
    resp = auth()
    if resp is True:
        con = sql.connect('student.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute('SELECT * FROM student')
        rows = cur.fetchall()
        return render_template('details.html', rows=rows)
    return redirect(url_for('login_page'))



@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login_page'))


if __name__ == "__main__":
    app.run(debug=True)