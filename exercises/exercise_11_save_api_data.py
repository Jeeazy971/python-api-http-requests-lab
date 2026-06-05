import requests
from pathlib import Path


def get_product(product_id):
    url = f"https://dummyjson.com/products/{product_id}"

    headers = {
        "Accept": "application/json",
        "User-Agent": "python-api-http-requests-lab/1.0"
    }

    response = requests.get(url, headers=headers, timeout=5)

    if response.status_code == 200:
        return response.json()

    return None


def create_product_report_content(product):
    return f"""Product report
    
Title: {product['title']}
Category: {product['category']}
Price: {product['price']}
Rating: {product['rating']}
Stock: {product['stock']}
Brand: {product.get('brand', 'Unknown')}
    """


def generate_product_file(product_content):
    output_folder = Path("data") / "output" / "reports"
    output_folder.mkdir(parents=True, exist_ok=True)
    report_path = output_folder / "product_report.txt"

    report_path.write_text(product_content, encoding="utf-8")
    return report_path


product = get_product(1)

if product is not None:
    new_product = create_product_report_content(product)
    product_report_file = generate_product_file(new_product)
    print("Product report generated:")
    print(product_report_file)
else:
    print("Product not found")
