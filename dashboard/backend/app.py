from flask import Flask
from flask_cors import CORS
from routes.events import events_bp

app = Flask(__name__)
CORS(app)

# Register API Blueprints
app.register_blueprint(events_bp, url_prefix="/api/events")

if __name__ == "__main__":
    app.run(debug=True)
