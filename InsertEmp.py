from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def new_employee():
    return render_template('employee2.html')

@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            id = request.form['id']
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            dept = request.form['dept']

            with sql.connect("database2.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO employee2 (id,name,addr,city,dept)"
                            "VALUES(?, ?, ?, ?, ?)",(id,nm,addr,city,dept))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "Error in insert operation."

        finally:
            return render_template("result1.html", msg=msg)
            con.close()


@app.route('/list1')
def list1():
    con = sql.connect('database2.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from employee2")

    rows = cur.fetchall();
    return render_template("list1.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)






