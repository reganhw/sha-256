from flask import Flask, render_template, request
from sha256 import sha256
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # POST
    if request.method == 'POST':
        user_input = request.form['user_input']
        try:
            result = sha256(user_input)
            return render_template('index.html', result = result)
        except Exception as e:
            error = str(e)
            return render_template('index.html', error=error)
    
    # GET
    return render_template('index.html', user_input = None, result = None, error = None)

if __name__ == '__main__':
    app.run(debug=True)