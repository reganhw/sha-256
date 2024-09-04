from flask import Flask, render_template, request, session, redirect, url_for, flash
from sha256 import sha256
app = Flask(__name__)
app.config.from_object('config')
#app.config.from_envvar('YOURAPPLICATION_SETTINGS')
app.secret_key = app.config["SECRET_KEY"] 

@app.route('/', methods=['GET', 'POST'])
def index():
    # POST
    if request.method == 'POST':
        user_input = request.form['user_input']
        try:
            result = sha256(user_input)
            session['result'] = result 
        except Exception as e:
            flash(str(e))
        return redirect(url_for('index'))
    
    # GET
    result = session.pop('result', None)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)