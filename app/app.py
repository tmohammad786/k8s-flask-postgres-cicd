from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App Running Successfully!"

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD']
        )
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

