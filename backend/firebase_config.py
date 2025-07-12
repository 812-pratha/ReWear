import pyrebase

firebase_config = {
    "apiKey": "AIzaSyD6ftd7Z4_s6NLVgWBx5EQFWpT4-UQ2G0o",
    "authDomain": "rewear-27971.firebaseapp.com",
    "projectId": "rewear-27971",
    "storageBucket": "rewear-27971.appspot.com",
    "messagingSenderId": "537941390901",
    "appId": "1:537941390901:web:ea93e54af3ebf43d4ba37c",
    "measurementId": "G-5G0JY9SEFV",
    "databaseURL": "" 
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
