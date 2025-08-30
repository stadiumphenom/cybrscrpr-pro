import csv
from datetime import datetime

def export_results(results):
    """
    Exports the results to a CSV file with a timestamped filename.
    Each result is written as a single line under the 'Content' column.
    """
    filename = f"scraped_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Content"])  # CSV header
        for item in results:
            writer.writerow([item])
# CSV/JSON/XLSX exporter logic placeholder
