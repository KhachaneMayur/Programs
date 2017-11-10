from flask import Blueprint, url_for, g, render_template
import flask_sijax

blueprint = Blueprint('myblueprint', __name__, url_prefix='/myblueprint', template_folder='templates')

@flask_sijax.route(blueprint, '/')
def index():
    def say_hi(obj_response):
        obj_response.alert('Hi there!')

    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sayHi', say_hi)
        return g.sijax.process_request()

    return render_template('page.html')