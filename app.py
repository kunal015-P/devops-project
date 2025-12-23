from flask import Flask, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )

@app.route("/")
def home():
    return "Flask App is Running!"

@app.route("/add")
def add_user():
    name = request.args.get("name", "Guest")
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    db.commit()
    cursor.close()
    db.close()
    return f"User {name} added successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
