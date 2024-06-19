from flask import Blueprint, render_template
from . import db

bp = Blueprint('actor', __name__, url_prefix = "/actores")

@bp.route("/")
def actores():
    actoresNyA = """
        SELECT first_name, last_name, actor_id FROM actor
        ORDER BY first_name, last_name ASC
    """
    con = db.get_db()
    res = con.execute(actoresNyA)
    actores = res.fetchall()
    pagina = render_template('actores.html', actores=actores)
    return pagina


@bp.route('/<int:id>')
def detalle(id):
    actoresNyA = """
        SELECT first_name, last_name FROM actor
        WHERE actor_id = ?
    """
    con = db.get_db()
    res = con.execute(actoresNyA,(id,))
    actor = res.fetchone()


    actoresNyA2 = """
        SELECT title AS titulo, f.film_id FROM film f
        JOIN film_actor fi ON f.film_id = fi.film_id
        WHERE fi.actor_id = ?
    """
    res = con.execute(actoresNyA2,(id,))
    lista_peliculas = res.fetchall()
    paginaActores = render_template('detalle_actor.html',
                                    actor=actor, 
                                    peliculas=lista_peliculas )

    return paginaActores

