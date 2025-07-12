from flask import Flask, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from routes.auth_routes import auth_bp
import os

# Load environment variables
load_dotenv()

# Set up Flask app
app = Flask(__name__, static_folder='../frontend', static_url_path='')
app.secret_key = "supersecretkey"  # Needed for sessions
CORS(app)

# Register blueprint for auth routes
app.register_blueprint(auth_bp)

# Serve index.html at root
@app.route('/index')
def home():
    return send_from_directory(app.static_folder, 'index.html')

# Serve login.html
@app.route('/login')
def login():
    return send_from_directory(app.static_folder, 'login.html')

# Serve register.html
@app.route('/register')
def register():
    return send_from_directory(app.static_folder, 'register.html')

# Serve static files (JS, CSS, images, etc.)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
