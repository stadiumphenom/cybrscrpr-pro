import csv
import json
import pandas as pd
from datetime import datetime
import os

EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

def export_to_csv(data, filename_prefix="scraped_results"):
    filename = f"{EXPORT_DIR}/{filename_prefix}_{timestamp()}.csv"
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    return filename

def export_to_json(data, filename_prefix="scraped_results"):
    filename = f"{EXPORT_DIR}/{filename_prefix}_{timestamp()}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return filename

def export_to_excel(data, filename_prefix="scraped_results"):
    filename = f"{EXPORT_DIR}/{filename_prefix}_{timestamp()}.xlsx"
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    return filename

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")
