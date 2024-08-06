from flask import Flask, render_template

gup = Flask(__name__)


# main route
@gup.route('/')
def gup_login():
    return render_template('landing.html')


if __name__ == "__main__":
    gup.run(debug=False, host='0.0.0.0')
