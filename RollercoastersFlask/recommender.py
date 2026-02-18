from flask import render_template
from config import ALLOWED_COASTERS
from security import validate_length
from flask import request
from flask import redirect, url_for

# ------------------ Helper function ------------------ #

def ask(step, data):
    return render_template("recommender.html", step=step, data=data)


# ------------------ Recommender functions ------------------ #


# ---------- Young_kids_recommender ---------- #
def young_kids_recommender(data):
    if "butterflies" not in data:
        return ask("butterflies", data)

    if data["butterflies"] == "yes":
        if "soaked" not in data:
            return ask("soaked", data)

        if data["soaked"] == "yes":
            return redirect(url_for("coaster_page", name="Atlantica_Supersplash"))

        if "system" not in data:
            return ask("system", data)

        coaster = "Alpen_Express" if data["system"] == "launch" else "Pegasus"
        return redirect(url_for("coaster_page", name=coaster))

    # butterflies == "no"
    return redirect(url_for("coaster_page", name="Ba_a_a_Express"))


# ---------- Kids_recommender ---------- #
def kids_recommender(data):
    if "exciting" not in data:
        return ask("exciting", data)

    if data["exciting"] == "yes":
        if "first_coaster" not in data:
            return ask("first_coaster", data)
        
        if data["first_coaster"] == "yes":
            return funny_recommender(data) 
        return redirect(url_for("coaster_page", name="Wodan"))
    return funny_recommender(data)


# ---------- Intense_recommender ---------- #
def intense_recommender(data):
    if "intense" not in data:
        return ask("intense", data)

    if data["intense"] == "yes":

        if "inversions" not in data:
            return ask("inversions", data)

        if data["inversions"] == "yes":

            if "comfortable_inversions" not in data:
                return ask("comfortable_inversions", data)

            coaster = "Voltron" if data["comfortable_inversions"] == "yes" else "Blue_Fire"
            return redirect(url_for("coaster_page", name=coaster))

        # inversions == no
        if "spin_wood" not in data:
            return ask("spin_wood", data)

        coaster = "Euromir" if data["spin_wood"] == "spinning_coaster" else "Wodan"
        return redirect(url_for("coaster_page", name=coaster))

    # intense == no
    return funny_recommender(data)


# ---------- High_recommender ---------- #
def high_recommender(data):
    if "very_high" not in data:
        return ask("very_high", data)

    if data["very_high"] == "yes":
        return redirect(url_for("coaster_page", name="Silverstar"))

    return intense_recommender(data)


# ---------- Funny_recommender ---------- #
def funny_recommender(data):
    if "funny" not in data:
        return ask("funny", data)

    if data["funny"] == "yes":

        if "indoor" not in data:
            return ask("indoor", data)

        if data["indoor"] == "yes":

            if "indoor_type" not in data:
                return ask("indoor_type", data)

            coaster = "Arthur" if data["indoor_type"] == "darkride" else "Cancan_Coaster"
            return redirect(url_for("coaster_page", name=coaster))

        # indoor == no
        if "soaked" not in data:
            return ask("soaked", data)

        if data["soaked"] == "yes":
            return soaked_recommender(data)

        if "rail_type" not in data:
            return ask("rail_type", data)

        coaster = "Schweizer_Bobbahn" if data["rail_type"] == "bobsled" else "Matterhorn_Blitz"
        return redirect(url_for("coaster_page", name=coaster))

    # funny == no
    return redirect(url_for("coaster_page", name="Alpen_Express"))

# ---------- Soaked_recommender ---------- #
def soaked_recommender(data):
    if "splash_type" not in data:
        return ask("splash_type", data)

    coaster = "Atlantica_Supersplash" if data["splash_type"] == "splash" else "Poseidon"
    return redirect(url_for("coaster_page", name=coaster))

