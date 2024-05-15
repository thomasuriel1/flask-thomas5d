from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)


@app.route('/actores')
def actores():
    actoresNyA = """
        SELECT first_name, last_name FROM actor
        ORDER BY first_name, last_name ASC
    """
    con = db.get_db()
    res = con.execute(actoresNyA)
    lista_actor = res.fetchall()
    paginaActores = render_template('actores.html', actores=lista_actor )

    return paginaActores

@app.route('/lenguaje')
def lenguaje():
    lenguaje = """
        SELECT name FROM language
        ORDER BY name ASC
    """
    con = db.get_db()
    res = con.execute(lenguaje)
    lista_lenguaje = res.fetchall()
    paginaLenguaje = render_template('lenguaje.html', lenguaje=lista_lenguaje )

    return paginaLenguaje
