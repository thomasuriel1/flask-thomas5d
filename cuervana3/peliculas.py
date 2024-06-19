from flask import Blueprint, render_template
from . import db

bp = Blueprint('peliculas', __name__, url_prefix = "/peliculas")

@bp.route("/")
def pelicula():
    peliculasNyA = """
        SELECT title, film_id FROM film
        ORDER BY title ASC
    """
    con = db.get_db()
    res = con.execute(peliculasNyA)
    peliculas = res.fetchall()
    pagina = render_template('peliculas.html', peliculas=peliculas)
    return pagina

@bp.route("/<int:id>")
def detallePeli(id):
    peliculasNyA = """
        SELECT description, rating, release_year, title FROM film
        WHERE film_id = ?
    """

    con = db.get_db()
    res = con.execute(peliculasNyA,(id,))
    peli = res.fetchone()


    peliculasNyA2 = """
        SELECT first_name, last_name, f.actor_id FROM film_actor f
        JOIN actor a ON a.actor_id = f.actor_id
        WHERE f.film_id = ?
    """
    res = con.execute(peliculasNyA2,(id,))
    lista_actores = res.fetchall()
    paginaPeliculas = render_template('detalle_peliculas.html',
                                    peli=peli, 
                                    actores=lista_actores )

    return paginaPeliculas