# Set your Spotify API credentials

import os
from flask import Flask, render_template, request
from utils import search_song



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        query = request.form["song"]
        result = search_song(query)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
