# Importing all dependences from the main
from main import app
from flask import render_template

# -------------- Defining routes --------------

# Homepage route
@app.route("/") # @ means a decorator. It adds an extra configuration to a function. In this case, the attribute represents the path after the domain
def homepage():
    return render_template("homepage.html")

# Infopage route
@app.route("/infos")
def infopage():
    return "Olá, mundo!"