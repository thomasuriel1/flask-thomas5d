from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

from . import actores
app.register_blueprint(actores.bp)

from . import lenguaje
app.register_blueprint(lenguaje.bp)


