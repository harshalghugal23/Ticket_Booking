from flask import Flask, request, jsonify
from models import db, Bookings
from config import Config
import uuid
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status":"ok"}), 200
    @app.route("/", methods=["GET"])
    def index():
        return jsonify({
            "message": "Welcome to the Ticket Booking API",
            "endpoints": {
                "/health": "Check health status",
                "/book": "POST - Create a new booking",
                "/view/<booking_id>": "GET - View booking details",
                "/cancel/<booking_id>": "DELETE - Cancel a booking"
            }
        })

    @app.route("/book", methods=["POST"])
    def book_ticket():
        data = request.get_json() or {}
        name = data.get("name")
        event = data.get("event", "default_event")
        if not name:
            return jsonify({"error":"name required"}), 400
        booking = Bookings(name=name, event=event)
        db.session.add(booking)
        db.session.commit()
        return jsonify({"booking_id": booking.id}), 201

    @app.route("/view/<booking_id>", methods=["GET"])
    def view_booking(booking_id):
        b = Bookings.query.get(booking_id)
        if not b:
            return jsonify({"error":"not found"}), 404
        return jsonify({
            "id": b.id,
            "name": b.name,
            "event": b.event,
            "created_at": b.created_at.isoformat()
        })

    @app.route("/cancel/<booking_id>", methods=["DELETE"])
    def cancel_booking(booking_id):
        b = Bookings.query.get(booking_id)
        if not b:
            return jsonify({"error":"not found"}), 404
        db.session.delete(b)
        db.session.commit()
        return jsonify({"status":"cancelled"}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
