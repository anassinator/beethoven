from flask import Flask, render_template, redirect

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdf', methods=['POST'])
def pdf():
    return redirect('static/notes.png')

if __name__=="__main__":
    app.run()
