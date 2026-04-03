# ---------- These are the imports required for this module ---------- #

from flask import Flask, request, render_template, redirect, url_for, abort

from config import ALLOWED_COASTERS, ALLOWED_KEYS
from security import validate_length, validate_tamper
from recommender import (
    young_kids_recommender, kids_recommender,
    intense_recommender, high_recommender
)

from routes import register_routes
from database import init_db
init_db()


app = Flask(__name__)

# ---------- Register all routes ---------- #

register_routes(app)

if __name__ == "__main__":
    app.run(debug=False)
