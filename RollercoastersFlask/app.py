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
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.after_request
def add_header(response):

# ---------- Tell the browser, not to save papes after visiting  ---------- #
    
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

# ---------- safety header against scripts ---------- #

    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response


# ---------- Prevents the website from being loaded in an iframe on another site without authorization (Clickjacking). ---------- #

def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY' 
    return response


# ---------- Register all routes ---------- #

register_routes(app)

if __name__ == "__main__":
    app.run(debug=False)
