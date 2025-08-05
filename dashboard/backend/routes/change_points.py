# dashboard/backend/routes/change_points.py
import os
import pandas as pd
from flask import Blueprint, jsonify

change_points_bp = Blueprint("change_points", __name__)


@change_points_bp.route("/api/change-points", methods=["GET"])
def get_change_points():
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
    file_path = os.path.join(ROOT_DIR, "data", "processed", "change_points.csv")
    if not os.path.exists(file_path):
        return jsonify({"error": "Change points file not found"}), 404

    df = pd.read_csv(file_path)
    return jsonify(df.to_dict(orient="records"))
