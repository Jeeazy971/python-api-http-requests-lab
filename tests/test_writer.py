from api_client_lab.writer import save_report


def test_save_report_writes_report_file(tmp_path):
    report_content = "API Products Report\nAverage price: 35.00"
    result = save_report(report_content, tmp_path)

    assert result.exists()
    assert result.name == "api_products_report.txt"
    assert result.read_text(encoding="utf-8") == report_content
    assert result.parent == tmp_path
