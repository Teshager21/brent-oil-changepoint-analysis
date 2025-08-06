import os
import pandas as pd
import json
from flask import Blueprint

# from datetime import timedelta

change_points_bp = Blueprint("change_points", __name__)

# load key events only once
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
path = os.path.join(ROOT_DIR, "data", "key_events.json")
with open(path) as f:
    key_events_raw = json.load(f)

ke_df = pd.DataFrame(
    [
        {"event_date": pd.to_datetime(date), "event": desc}
        for date, desc in key_events_raw.items()
    ]
)


@change_points_bp.route("/change-points", methods=["GET"])
def get_change_points():
    # Load change points on every request
    path2 = os.path.join(ROOT_DIR, "data", "processed", "change_points.csv")
    cp_df = pd.read_csv(path2)
    cp_df["change_point_date"] = pd.to_datetime(cp_df["change_point_date"])

    def find_closest_event(cp_date, window=60):
        time_deltas = abs(ke_df["event_date"] - cp_date)
        min_delta = time_deltas.min()
        if min_delta <= pd.Timedelta(days=window):
            matched_index = time_deltas.idxmin()
            return (
                ke_df.loc[matched_index, "event_date"],
                ke_df.loc[matched_index, "event"],
            )
        else:
            return None, None

    cp_df["matched_event_date"] = None
    cp_df["event"] = None

    for i, row in cp_df.iterrows():
        matched_date, event = find_closest_event(row["change_point_date"])
        cp_df.at[i, "matched_event_date"] = matched_date
        cp_df.at[i, "event"] = event

    cp_df["change_point_date"] = cp_df["change_point_date"].dt.strftime("%Y-%m-%d")
    cp_df["matched_event_date"] = pd.to_datetime(
        cp_df["matched_event_date"], errors="coerce"
    )
    cp_df["matched_event_date"] = cp_df["matched_event_date"].dt.strftime("%Y-%m-%d")

    return cp_df.where(pd.notnull(cp_df), None).to_dict(orient="records")
