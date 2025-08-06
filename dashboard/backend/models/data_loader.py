# models/data_loader.py

import pandas as pd
import os


def load_events():
    # Go up two levels from the current file
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
    path = os.path.join(ROOT_DIR, "data", "raw", "events.csv")
    return pd.read_csv(path)
