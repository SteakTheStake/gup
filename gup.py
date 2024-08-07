from flask import Flask, render_template, session, redirect, url_for

gup = Flask(__name__)
gup.secret_key = '1209082503'

# Session configuration
gup.config['SESSION_TYPE'] = 'filesystem'
gup.config['SESSION_PERMANENT'] = False


# Main route
@gup.route('/')
def gup_home():
    if 'logged_in' in session and session['logged_in']:
        return render_template('feed.html')
    else:
        return render_template('landing.html')


# Route to handle login (for example purposes)
@gup.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('gup_home'))


# Route to handle logout (for example purposes)
@gup.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('gup_home'))


if __name__ == "__main__":
    gup.run(debug=False, host='0.0.0.0')
