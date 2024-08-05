from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

gup = Flask(__name__)


# main route
@gup.route('/')
def gup_login():
    return render_template('index.html')


if __name__ == "__main__":
    gup.run()
