from flask import Flask, render_template

app = Flask(__name__)

@app.route("/map")
def map():
    return render_template("map.html")

app.run('0.0.0.0')