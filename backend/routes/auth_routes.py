from flask import Blueprint, request, jsonify, session
import requests
import os


auth_bp = Blueprint('auth', __name__)
FIREBASE_API_KEY = os.getenv('FIREBASE_API_KEY')  # Set in .env or environment


# Firebase endpoints
SIGNUP_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
LOGIN_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"


@auth_bp.route("/signup", methods=["POST"])
def signup():
   data = request.json
   email = data.get("email")
   password = data.get("password")


   payload = {
       "email": email,
       "password": password,
       "returnSecureToken": True
   }


   response = requests.post(SIGNUP_URL, json=payload)


   if response.status_code == 200:
       return jsonify({"message": "Signup successful", "user": response.json()}), 200
   else:
       return jsonify({"error": response.json().get("error", {}).get("message", "Signup failed")}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
   data = request.json
   email = data.get("email")
   password = data.get("password")


   payload = {
       "email": email,
       "password": password,
       "returnSecureToken": True
       }


   response = requests.post(LOGIN_URL, json=payload)


   if response.status_code == 200:
       res_data = response.json()
       session["user"] = {
           "email": email,
           "idToken": res_data["idToken"]
       }
       return jsonify({"message": "Login successful", "user": session["user"]}), 200
   else:
       return jsonify({"error": response.json().get("error", {}).get("message", "Login failed")}), 401


@auth_bp.route("/logout", methods=["POST"])
def logout():
   session.pop("user", None)
   return jsonify({"message": "Logged out"}), 200