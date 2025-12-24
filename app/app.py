from flask import Flask, jsonify, request
import logging
import os

app = Flask(__name__)

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


@app.route("/", methods=["GET"])
def home():
    logger.info("Home endpoint accessed")
    return jsonify({
        "message": "Flask app is running"
    })


@app.route("/health", methods=["GET"])
def health():
    logger.info("Health check called")
    return jsonify({
        "status": "UP"
    }), 200


@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    logger.info(f"Echo endpoint called with data: {data}")
    return jsonify({
        "received": data
    }), 200


@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {str(e)}")
    return jsonify({
        "error": "Internal Server Error"
    }), 500


if __name__ == "__main__":
    logger.info("Starting Flask application")
    app.run(host="0.0.0.0", port=8000)
