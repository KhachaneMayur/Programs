from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mkhachane1000@gmail.com'
app.config['MAIL_PASSWORD'] = '8888543401'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello', sender='mkhachane1000@gmail.com', recipients=['mkhachane1000@gmail.com'])
    msg.body = "Hello Mayur I'am Laukik"
    mail.send(msg)
    return "Email Sent"

if __name__ == "__main__":
    app.run(debug= True)