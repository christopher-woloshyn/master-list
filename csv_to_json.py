import json
import pandas as pd


def convert_rows(df):
    """Convert each activity row to JSON format."""
    result = {}
    for name in df["activity_name"]:
        result[name] = convert_columns(df, name)

    return result

def convert_columns(df, name):
    """Convert each column data for each row into JSON format."""
    result = {}
    for key in df.columns:
        if key != "activity_name":
            value = df.loc[df["activity_name"] == name][key].values[0].item()
            result[key] = value

    return result

def export(dictionary, fname):
    """Export output dictionary as a JSON file."""
    with open(fname, 'w') as f:
        json.dump(dictionary, f, indent=2)
    f.close()

def csv_to_json():
    """Convert activities.csv to activities.json"""
    data = pd.read_csv('activities.csv')
    output = convert_rows(data)
    export(output, 'activities.json')

def main():
    csv_to_json()

if __name__ == '__main__':
    main()
