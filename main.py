# Initializing the project
from flask import Flask

app = Flask(__name__)

# -------------- Defining routes --------------

# Homepage route
@app.route("/") # @ means a decorator. It adds an extra configuration to a function
def homepage():
    return "Olá, mundo!"

# This "if" were created to guarantee that the app runs just when the main.py is directly executed 
if __name__ == "__main__": 
    app.run()

