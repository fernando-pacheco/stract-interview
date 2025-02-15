import os
from flask import Flask
from src.routes import Routes
from src.stract_rest import StractRest

app = Flask(__name__)
stract_rest = StractRest(os.environ)
routes = Routes(app, stract_rest) 

if __name__ == "__main__":
    app.run()
