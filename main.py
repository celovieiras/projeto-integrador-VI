from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/empresa")
def empresa():
    return render_template("empresa.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def cadastro():
    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)