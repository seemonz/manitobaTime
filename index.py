from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/writings")
def writings():
	return render_template('writings.html')


# TODO should make this into a set of writing objects in the future,, additional 
@app.route("/writings/aStringandaBalloon")
def aStringandaBalloon():
	return render_template('writings/aStringandaBalloon.html')
