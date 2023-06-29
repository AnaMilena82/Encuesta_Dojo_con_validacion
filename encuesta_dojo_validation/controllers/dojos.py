from flask import render_template, request, redirect, session, url_for, flash
from __init__ import app
from models.dojo import Dojo


@app.route('/', methods = ['GET'])    
def get_encuesta():
    return render_template("index.html")


@app.route('/', methods = ['POST'])    
def post_encuesta():
    data = {
        "name": request.form["name"],
        "location" : request.form["location"],
        "language": request.form["language"],
        "comment": request.form["comment"],
    }
    if not Dojo.validate_dojo(request.form):
        # redirigir a la ruta donde se renderiza el formulario de dojo
        return redirect('/')
    dojo = Dojo.new_dojo(data)
    flash("Dojo ingresado satisfactoriamente", "success")
    
    return redirect(url_for('result'))
    

@app.route('/result')
def result():
    #Obtener los datos almacenados en la variable de sesión
    dojos = Dojo.get_all_dojo()
         
    return render_template('result.html', dojos=dojos)

