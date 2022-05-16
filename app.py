from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/skills")
def skills():
    return render_template('skills.html')