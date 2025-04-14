from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configuration settings from 'instance/config.py'
    app.config.from_object('instance.config')

    # Register routes (you'll create this file next)
    from .routes import main
    app.register_blueprint(main)

    return app
