from flask import Flask
from flask_babel import Babel, _

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'  # Needed for session

    babel = Babel(app)

    # Make _ available in Jinja templates
    app.jinja_env.globals['_'] = _

    from .routes import main
    app.register_blueprint(main)

    return app