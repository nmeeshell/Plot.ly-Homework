from flask import Flask, jsonify, render_template
import csv
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
  with open("")as file:
    dict_reader = csv.DictReader(file)
    return jsonify(list(dict_reader))

  if__name__=="__main__":
    app.run(debug=True)