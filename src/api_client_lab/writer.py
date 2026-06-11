from pathlib import Path

def save_report(report_content):
    report_folder = Path("data") / "output" / "reports"
    report_folder.mkdir(parents=True, exist_ok=True)
    api_products_report_file = report_folder / "api_products_report.txt"

    api_products_report_file.write_text(report_content, encoding="utf-8")
    return api_products_report_file
