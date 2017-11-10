import os
from flask import Flask, redirect, url_for
import flask_sijax
from myblueprint import blueprint

app = Flask(__name__)

app.config["SIJAX_STATIC_PATH"] = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app.config["SIJAX_JSON_URI"] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)

app.register_blueprint(blueprint)

@app.route('/')
def index():
    return redirect(url_for('myblueprint.index'))

if __name__ == '__main__':
    app.run(debug=True)