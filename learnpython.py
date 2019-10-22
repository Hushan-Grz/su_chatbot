import flask
from flask import Blueprint, request, jsonify ,Response , send_file , make_response
app = Flask(__name__)

@app.route('/', methods=[GET,POST])

def hello():
    return 'Hello, World!'

if __name__==’__main__’:
		app.run(debug=TRUE)           # Real time updation at the webpage

def basic():
    #request.method and request.form
    if request.mothed == 'POST':
         request.form['name']
         return 'validation successful'

	return render_template(‘first.html’)