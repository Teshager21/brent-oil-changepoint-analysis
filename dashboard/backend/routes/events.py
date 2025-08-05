from flask import Blueprint, jsonify
import pandas as pd
import os

events_bp = Blueprint("events", __name__)


@events_bp.route("/", methods=["GET"])
def get_events():
    # Go up two levels from the current file
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
    path = os.path.join(ROOT_DIR, "data", "raw", "events.csv")
    df = pd.read_csv(path)
    return jsonify(df.to_dict(orient="records"))
