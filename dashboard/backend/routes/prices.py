# dashboard/backend/routes/prices.py
import os
import pandas as pd
from flask import Blueprint, jsonify

prices_bp = Blueprint("prices", __name__)


@prices_bp.route("/api/prices", methods=["GET"])
def get_prices():
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
    # file_path = os.path.abspath(
    #     os.path.join(os.path.dirname(__file__), "../../data/processed/prices.csv")
    # )
    file_path = os.path.join(ROOT_DIR, "data", "raw", "BrentOilPrices.csv")

    if not os.path.exists(file_path):
        return jsonify({"error": "Prices file not found"}), 404

    df = pd.read_csv(file_path)
    return jsonify(df.to_dict(orient="records"))
