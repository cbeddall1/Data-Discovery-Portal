from flask import Flask 

from config import Config 

 

def create_app(config_class=Config): 

    # Templates are stored under app/static/templates in this project.
    app = Flask(__name__, template_folder='static/templates', static_folder='static') 

    app.config.from_object(config_class) 

    from app.routes import main 

    app.register_blueprint(main) 

    return app 