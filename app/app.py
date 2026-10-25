import os

import psycopg
from flask import Flask, jsonify

app = Flask(__name__)

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://app_user:change_me_local_only@localhost:5432/app_db"
)


@app.route("/")
def home():
    return jsonify({"message": "Python app is running"}), 200

@app.route("/db")
def db_status():
    try:
        with psycopg.connect(DATABASE_URL, connect_timeout=3) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT version()")
                version = cursor.fetchone()[0]

        return jsonify({
            "database": "connected",
            "version": version,
        }), 200

    except psycopg.Error:
        app.logger.exception("Database connection failed")
        return jsonify({"database": "unavailable"}), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
