from flask import Flask, request
from caesar import encryption

import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['get'])
def index():
    template = jinja_env.get_template('encrypt_template.html')
    return template.render()



@app.route("/", methods=['post'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']

    new_message = encryption(text, rot)

    template = jinja_env.get_template('encrypt_template.html')
    return template.render(text=new_message)

app.run()

