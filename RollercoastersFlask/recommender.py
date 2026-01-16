from flask import render_template
from config import ALLOWED_COASTERS
from security import validate_length
from flask import request

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
            return render_template("coasters/Atlantica_Supersplash.html")

        if "system" not in data:
            return ask("system", data)

        return render_template(
            "coasters/Alpen_Express.html" if data["system"] == "launch"
            else "coasters/Pegasus.html"
        )

    return render_template("coasters/Ba_a_a_Express.html")

# ---------- Kids_recommender ---------- #
def kids_recommender(data):
    if "exciting" not in data:
        return ask("exciting", data)

    if data["exciting"] == "yes":
        if "first_coaster" not in data:
            return ask("first_coaster", data)

        return funny_recommender(data) if data["first_coaster"] == "yes" else render_template("coasters/Wodan.html")
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

            return render_template(
                "coasters/Voltron.html" if data["comfortable_inversions"] == "yes"
                else "coasters/Blue_Fire.html"
            )

        if "spin_wood" not in data:
            return ask("spin_wood", data)

        return render_template(
            "coasters/Euromir.html" if data["spin_wood"] == "spinning_coaster"
            else "coasters/Wodan.html"
        )

    return funny_recommender(data)

# ---------- High_recommender ---------- #
def high_recommender(data):
    if "very_high" not in data:
        return ask("very_high", data)

    if data["very_high"] == "yes":
        return render_template("coasters/Silverstar.html")

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

            return render_template(
                "coasters/Arthur.html" if data["indoor_type"] == "darkride"
                else "coasters/Cancan_Coaster.html"
            )

        if "soaked" not in data:
            return ask("soaked", data)

        if data["soaked"] == "yes":
            return soaked_recommender(data)

        if "rail_type" not in data:
            return ask("rail_type", data)

        return render_template(
            "coasters/Schweizer_Bobbahn.html" if data["rail_type"] == "bobsled"
            else "coasters/Matterhorn_Blitz.html"
        )

    return render_template("coasters/Alpen_Express.html")


# ---------- Soaked_recommender ---------- #
def soaked_recommender(data):
    if "splash_type" not in data:
        return ask("splash_type", data)

    return render_template(
        "coasters/Atlantica_Supersplash.html" if data["splash_type"] == "splash"
        else "coasters/Poseidon.html"
    )
