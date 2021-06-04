from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "pokemon"

debug = DebugToolbarExtension(app)

@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route('/greet')
def greets():
    username = request.args["username"]
    return render_template("greet.html", username=username)