from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

messages = [
    "Richard: Hi everyone",
    "Everyone: Hi Richard"
    ]
    
@app.route("/")
def show_hi():
    return render_template("index.html", messages=messages)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)