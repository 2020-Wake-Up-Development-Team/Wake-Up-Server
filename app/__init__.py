import os
from flask import Flask
from .db import init_app

def create_app(testconfig = None):

    app = Flask(__name__, instance_relative_config=False)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

        #apply blueprint to the app
    from .main.controller import auth_controller, material_controller, barcode_controller

    app.register_blueprint(auth_controller.api)
    app.register_blueprint(material_controller.api)
    app.register_blueprint(meeting_controller.api)

    db.init_app(app)
    
    return app