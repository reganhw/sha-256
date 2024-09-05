from flask import Flask, render_template, request, session, redirect, url_for, flash
from os import environ
from sha256 import sha256

app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    # POST
    if request.method == 'POST':
        user_input = request.form['user_input']
        try:
            result = sha256(user_input)          # calculate hash
            session['result'] = result           # set result for session
        except Exception as e:
            flash(str(e))                        # display errors
        return redirect(url_for('index'))        # redirect
    
    # GET
    result = session.pop('result', None)         # retrieve and clear 'result'
    return render_template('index.html', result=result) 

if __name__ == '__main__':
    app.run(debug=True, port=8000)