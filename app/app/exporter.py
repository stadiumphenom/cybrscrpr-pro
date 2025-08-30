
import pandas as pd

def export_csv(data, filename="export.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    return filename

def export_json(data, filename="export.json"):
    import json
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    return filename

def export_excel(data, filename="export.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    return filename
