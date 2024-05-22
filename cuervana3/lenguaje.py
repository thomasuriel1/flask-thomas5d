from flask import Blueprint, render_template
from . import db

bp = Blueprint('lenguaje', __name__, url_prefix = "/lenguaje")


@bp.route('/')
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
