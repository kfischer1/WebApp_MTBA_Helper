from flask import Flask, render_template, request
from MBTA_helper1 import alert_user

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        stop, d = alert_user(location)
        if stop:
            return render_template('result.htm', stop= stop, distance = d)
    return render_template("home.htm")



if __name__ == "__main__":
    app.run()











