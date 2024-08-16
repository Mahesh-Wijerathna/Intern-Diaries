from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(user_bp, url_prefix='/api/user')
#  send hello world for root get method
@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=True, port=5000)
