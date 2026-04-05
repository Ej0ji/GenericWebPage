# Initializing the project
from flask import Flask

app = Flask(__name__)

# Importing all dependencies from the views
from views import *

# This "if" were created to guarantee that the app runs just when the main.py is directly executed 
if __name__ == "__main__": 
    app.run()

