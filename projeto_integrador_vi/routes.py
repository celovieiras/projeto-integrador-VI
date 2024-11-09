#rotas do site
from flask import render_template, url_for
from projeto_integrador_vi import app

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
