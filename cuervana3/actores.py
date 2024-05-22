from flask import Blueprint, render_template
from . import db

bp = Blueprint('actor', __name__, url_prefix = "/actores")


@bp.route('/')
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
