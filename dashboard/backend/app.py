from flask import Flask
from flask_cors import CORS
from routes.prices import prices_bp
from routes.change_points import change_points_bp
from routes.events import events_bp

app = Flask(__name__)
CORS(app)

# Register API Blueprints
app.register_blueprint(prices_bp)
app.register_blueprint(change_points_bp)
app.register_blueprint(events_bp, url_prefix="/api/events")

if __name__ == "__main__":
    app.run(debug=True)
