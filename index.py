from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/simonPelletier")
def simonPelletier():
	return render_template('simonPelletier.html')

@app.route("/writings")
def writings():
	return render_template('writings.html')

@app.route("/photos")
def photos():
	return render_template('photos.html')

@app.route("/art")
def art():
	return render_template('art.html')




# ====== WRITINGS =======
# TODO should make this into a set of writing objects in the future
@app.route("/writings/aStringandaBalloon")
def aStringandaBalloon():
	return render_template('writings/aStringandaBalloon.html')

@app.route("/writings/twentyThousandLeagues")
def twentyThousandLeagues():
	return render_template('writings/twentyThousandLeagues.html')

@app.route("/writings/dontPontificate")
def dontPontificate():
	return render_template('writings/dontPontificate.html')
