from flask import Flask

def create_app():
    print("Creating Flask app")
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    print("Blueprint registered")

    return app
