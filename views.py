# Importing all dependences from the main
from main import app

# -------------- Defining routes --------------

# Homepage route
@app.route("/") # @ means a decorator. It adds an extra configuration to a function
def homepage():
    return "Olá, mundo!"