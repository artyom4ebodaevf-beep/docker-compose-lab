import os
import time

import psycopg
from flask import Flask, jsonify

app = Flask(__name__)

DATABASE_URL = os.environ["DATABASE_URL"]

@app.get("/")
def index():
    return jsonify({"message": "Python app is running"})

@app.get("/db")
def database_status():
    try:
        with psycopg.connect(DATABASE_URL, connect_timeout=3) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version()")
                version = cur.fetchone()[0]

        return jsonify({"database": "connected", "version": version})
    except Exception:
        app.logger.exception("Database connection failed")
        return jsonify({"database": "unavailable"}), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
