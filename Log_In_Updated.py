from flask import Flask, redirect, render_template, request, session, url_for, json
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'random string'




def auth():
    if session.get('user') and session.get('pass') :
        return True
    return redirect(url_for('login_page'))



@app.route('/login_page')
def login_page():
    return render_template('login.html')



@app.route('/login', methods=['POST'])
def login():
    session['user'] = request.form['username']
    session['pass'] = request.form['password']
    if session['user'] == 'admin' and session['pass'] == 'admin':
        return redirect(url_for('details'))
    else:
        return "Invalid username & password. Please try again!.  <a href='/login_page'>Log In</a>"


#@app.route('/details')
#def details():
#    resp = auth()
#    if resp is True:
#        con = sql.connect('student.db')
#        con.row_factory = sql.Row
#        cur = con.cursor()
#        cur.execute('SELECT * FROM student')
#        rows = cur.fetchall()
#        return render_template('details.html', rows=rows)
#    else:
#        return redirect(url_for('login_page'))

@app.route('/details')
def details():
    resp = auth()
    if resp is True:
        con = sql.connect('student.db')
        cur = con.cursor()
        cur.execute('''SELECT * FROM student WHERE RollNo<=10''')
        row_headers = [x[0] for x in cur.description]
        rv = cur.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data) + "<a href='/logout'>Log_Out</a>"
    return redirect(url_for('login_page'))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login_page'))


if __name__ == "__main__":
    app.run(debug=True)