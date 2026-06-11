from api_client_lab.client import get_products
from api_client_lab.analyzer import (
    calculate_average_price,
    find_most_expensive_product,
    find_lowest_stock_product,
)
from api_client_lab.report import create_report
from api_client_lab.writer import save_report

def main():
    data = get_products(10, 0)


    if data is not None:
        products = data["products"]

        average_price = calculate_average_price(products)
        most_expensive_product = find_most_expensive_product(products)
        lowest_stock_product = find_lowest_stock_product(products)

        report_content = create_report(
            data,
            average_price,
            most_expensive_product,
            lowest_stock_product
        )

        report_path = save_report(report_content)

        print("API products report generated:")
        print(report_path)
    else:
        print("Could not generate report.")
    
if __name__ == "__main__":
    main()