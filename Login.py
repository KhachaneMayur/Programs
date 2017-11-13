from flask import Flask,request,flash,render_template,redirect,url_for
app = Flask(__name__)
app.secret_key = 'rondam string'

@app.route('/',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != '1234':
            print  "Invalid username & passsword, Please try again!"
        else:
            flash('You are Successfully Login')
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)