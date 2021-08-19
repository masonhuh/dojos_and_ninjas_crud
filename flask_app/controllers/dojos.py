from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def view_dojo():
    dojos = Dojo.get_dojos()
    return render_template("index.html", dojos = dojos)

@app.route('/ninjas')
def ninja():
    dojos = Dojo.get_dojos()
    return render_template("ninjas.html", dojos = dojos)

@app.route('/dojos/<int:dojo_id>')
def dojo_info(dojo_id):
    data = {
        'dojo_id': dojo_id
    }
    ninjas = Ninja.get_ninjas(data)
    return render_template('dojo_info.html', ninjas = ninjas)

@app.route('/dojos/create', methods =['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')

@app.route('/ninjas/create', methods =['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")
