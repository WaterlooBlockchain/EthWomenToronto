from flask import Flask


def create_app(test_config=None):
    application = Flask(__name__)
    
    from frontend.blueprints.collection import collection

    application.register_blueprint(collection)
    @application.route('/')
    def home():
        return 'Hello World'
        
    return application
