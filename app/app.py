from flask import Flask

from blueprints.page import page


def create_app():
    """
    Create a Flask application using the app factory pattern.
    
    :return: Flask app
    """
    app = Flask(__name__)

    app.register_blueprint(page)

    app.run(host='0.0.0.0', port=5000, debug=True)
    
    return app

if __name__ == '__main__': create_app()

