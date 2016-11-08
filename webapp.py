from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("home.htm")

@app.route('/hello')
def hello():
    return "Hello World"


if __name__ == "__main__":
    app.run()





