from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = [planet.to_json() for planet in planets]

        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(
            name=request_body["name"], description=request_body["description"]
        )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)
