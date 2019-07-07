from flask import Flask, render_template
from sklearn.externals import joblib

app = Flask(__name__)

@app.route("/")
def index():
	prediction=469658.5
	
	return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
	model = joblib.load('regr.pkl')
	app.run(debug=True)