# Copyright (c) 2021 Veera Lupunen

from . import app
from .db import db
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import secrets

@app.route("/admin")
def index():
    return render_template("index.html")
    
    
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT password, id FROM aicb.admin WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    
    if user == None:
        return render_template("index.html", message=("Oijoi, jotain meni pieleen! Tarkista, että kirjoitit tunnuksesi oikein."))
    else:
        hash_value = user[0]
        if check_password_hash(hash_value,password):
            session["username"] = username
            session["id"] = user[1]
            session["csrf_token"] = secrets.token_hex(18)
            return redirect("/settings")
        else:
            return render_template("index.html", message=("Oijoi! Tarkista, että kirjoitit salasanasi oikein."))
           
            
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/admin")
    
    
@app.route("/settings", methods=["POST", "GET"])
def settings():
    return render_template("settings.html")
    
    
@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    
    if len(username) > 25 or len(username) < 3:
        return render_template("index.html", message=("Liian lyhyt tai pitkä käyttäjänimi! Nimen tulee olla vähintään 3 merkkiä ja enintään 25 merkkiä pitkä."))
    
    sql = "SELECT COUNT(id) FROM aicb.admin WHERE username=(:username)"
    result = db.session.execute(sql, {"username":username})
    count = result.fetchone()[0]
    
    if count > 0:
        return render_template("index.html", message=("Voi harmi! Joku ehti jo varata tämän tunnuksen."))
    
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    
    val_result = validate_password(password1, password2)
    
    if val_result is not None:
        return render_template("index.html", message=val_result)
    
    hash_value = generate_password_hash(password1)

    sql = "INSERT INTO aicb.admin (username, password) VALUES(:username, :password)"
    db.session.execute(sql, {"username":username,"password":hash_value})
    db.session.commit()

    return render_template("index.html", message=("Rekisteröityminen onnistui!"))
    
    
def validate_password(password1, password2):
    if len(password1) < 8:
        return("Liian lyhyt salasana! Salasanan pitää olla vähintään 8 merkin pituinen.")
    
    if password1 != password2:
        return("Salasanat eivät täsmää!")
        
    return None
    
    
@app.route("/")
def home():
    return render_template("home.html")
    
    
@app.route("/join",  methods=["POST"])
def join():
    name = request.form["name"]
    code = request.form["code"]
    if name=="":
        return render_template("home.html", name=name, note="Kirjoita nimesi alla olevaan kentään.")
    elif "\"" in name:
        return render_template("home.html", name=name, note="Et voi käyttää tätä nimeä. Keksi jokin muu.")
    elif code=="":
        return render_template("home.html", code=code, note="Lisää opettajalta saamasi koodi alla olevaan kenttään.")
    else:
        #TODO: kooditsekki: ihmis- vai tekoälykoodi
        session["name"] = name
        session["room"] = code
        if code=="ihminen":
            session["ai"] = False
        else:
            session["ai"] = True
        return render_template("chat.html", name=name)
    
    
@app.route("/codes",  methods=["GET", "POST"])
def create_codes():
    return render_template("codes.html")
    
    
@app.route("/database",  methods=["GET", "POST"])
def update_database():
    return render_template("database.html")
