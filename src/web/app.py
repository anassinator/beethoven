from flask import Flask, render_template

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
	return render_template('index.html')

if __name__=="__main__":
	app.run()