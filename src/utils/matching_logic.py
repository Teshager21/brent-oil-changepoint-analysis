import pandas as pd
from datetime import timedelta

events_df = pd.read_csv("data/raw/events.csv", parse_dates=["event_date"])
changepoints = pd.to_datetime(
    ["2008-10-01", "2011-03-10", "2014-11-05", "2020-03-10", "2022-02-28"]
)

# Allowing a few days of tolerance (±15 days) for match
tolerance = timedelta(days=15)


def match_event(date):
    matches = events_df[
        (events_df["event_date"] >= date - tolerance)
        & (events_df["event_date"] <= date + tolerance)
    ]
    return matches[["event_name", "description"]] if not matches.empty else None


for date in changepoints:
    print(f"\nChange Point: {date.date()}")
    matched = match_event(date)
    if matched is not None:
        print("Matched Event(s):")
        print(matched.to_string(index=False))
    else:
        print("No event matched in window.")
