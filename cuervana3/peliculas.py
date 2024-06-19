from flask import Blueprint, render_template
from . import db

bp = Blueprint('peliculas', __name__, url_prefix = "/peliculas")

@bp.route("/")
def pelicula():
    peliculasNyA = """
        SELECT title FROM film
        ORDER BY title ASC
    """
    con = db.get_db()
    res = con.execute(peliculasNyA)
    peliculas = res.fetchall()
    pagina = render_template('peliculas.html', peliculas=peliculas)
    return pagina