from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes.auth_routes import auth_bp

load_dotenv()  # 👈 Load from .env

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for sessions
CORS(app)
app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return "ReWear backend running!"

if __name__ == "__main__":
    app.run(debug=True)
