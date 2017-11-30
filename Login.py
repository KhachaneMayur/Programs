from flask import Flask, redirect, render_template, request, session, url_for, json
import sqlite3 as sql,  urlparse
import urllib

app = Flask(__name__)
app.secret_key = 'random string'


def auth(url):
    if session.get('user') is None and session.get('pass') is None:
        return redirect(url_for('login_page')+"?url="+url)
    return True


@app.route('/login_page')
def login_page():
    url = request.url
    parsed = urlparse.urlparse(url)
    ur = parserd.query
    ul = urllib.unquote(ur).decode('utf8')
    x = ul.strip('url=')
    return render_template('login.html',next=x)


@app.route('/login', methods=['POST','GET'])
def login():
    con = sql.connect('admin.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM admin WHERE username =? and password =?',(request.form['username'],request.form['password']))
    rows = cur.fetchall()
    if len(rows)== 1:
        session['user'] = request.form['username']
        session['pass'] = request.form['password']
        return redirect(request.form['url'])
    else:
        return redirect(url_for('login_page'))


@app.route('/<details>', defaults={'rollno' : None})
@app.route('/<details>/<rollno>')
def details(details, rollno):
    resp = auth(url=request.url)
    if resp is True:
        con = sql.connect('student.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute('SELECT * FROM student WHERE RollNo = ?',(rollno,))
        rows = cur.fetchall()
        return render_template('details.html', rows=rows)
    return resp



@app.route('/details')
def info():
    resp = auth(url=request.url)
    if resp is True:
        con = sql.connect('student.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute('''SELECT * FROM student''')
        row_headers = [x[0] for x in cur.description]
        rv = cur.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data) + "<a href='/logout'>Log_Out</a>"
    return resp




@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login_page'))


if __name__ == "__main__":
    app.run(debug=True)
