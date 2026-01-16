from flask import render_template, request, redirect, url_for, abort
from config import ALLOWED_COASTERS, ALLOWED_KEYS
from security import validate_length, validate_tamper
from recommender import (
    young_kids_recommender, kids_recommender,
    intense_recommender, high_recommender
)
from extensions import limiter
from database import add_coaster_to_db, get_all_coasters


def register_routes(app):

    # ---------- Undoing actions ---------- #
    @app.route("/undo/<key>")
    def undo(key):
        if key not in ALLOWED_KEYS:
            return render_template("error.html", error="Invalid undo request ❌")

        data = request.args.to_dict()
        data.pop(key, None)
        return redirect(url_for("recommender", **data))

    # ---------- Home Redirect ---------- #
    @app.route("/")
    def home():
        return redirect(url_for("recommender"))

    # ---------- Coaster pages ---------- #
    @app.route("/coaster/<name>")
    def coaster_page(name):
        if name not in ALLOWED_COASTERS:
            abort(404)
        return render_template(f"coasters/{name}.html", coaster=name)


    # ---------- Recommender ---------- #
    @app.route("/recommender", methods=["GET", "POST"])
    @limiter.limit("10 per minute")
    def recommender():
        data = request.values.to_dict()

        tamper_error = validate_tamper(data)
        if tamper_error:
            return render_template("error.html", error=tamper_error)

        if "length" not in data:
            return render_template("recommender.html", step="length", data=data)

        length = validate_length(data.get("length"))
        if length is None:
            return render_template("error.html", error="Invalid or unrealistic height ❌")

        if length < 100:
            return render_template("error.html", error="Too short for these rollercoasters ❌")
        if length < 120:
            return young_kids_recommender(data)
        if length < 130:
            return kids_recommender(data)
        if length < 140:
            return intense_recommender(data)
        if length < 195:
            return high_recommender(data)

        return render_template("error.html", error="Too tall ❌")

    # ---------- Favorites List (SQL) ---------- #
    @app.route("/add_to_list")
    def add_to_list():
        coaster = request.args.get("coaster")
        add_coaster_to_db(coaster)
        return redirect(url_for("show_list"))

    @app.route("/list")
    def show_list():
        items = get_all_coasters()
        return render_template("list.html", items=items)

