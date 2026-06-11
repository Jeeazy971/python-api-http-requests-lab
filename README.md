# Python API Client Lab

A progressive Python learning project focused on consuming HTTP APIs with `requests`, handling JSON responses, analyzing API data, and generating local reports.

The project starts with small isolated exercises and ends with a refactored API client package using a clean `src/` structure.

## Project goals

This project was built to strengthen the fundamentals of API consumption in Python.

It covers:

```text
- HTTP request basics
- GET requests
- HTTP status codes
- JSON response handling
- query parameters
- HTTP headers
- POST requests with JSON payloads
- request timeouts
- basic API error handling
- reusable API client functions
- saving API data into local files
- refactoring a script into a structured Python package
```

## Features

```text
- Fetch product data from the DummyJSON API
- Send query parameters such as limit and skip
- Read and process JSON responses
- Calculate the average product price
- Find the most expensive product
- Find the product with the lowest stock
- Generate a text report from API data
- Save the generated report with pathlib
- Organize the final code into a reusable package
```

## Project structure

```text
python-api-http-requests-lab/
├── exercises/
│   ├── exercise_01_http_basics.py
│   ├── exercise_02_get_request.py
│   ├── exercise_03_status_code.py
│   ├── exercise_04_json_response.py
│   ├── exercise_05_query_params.py
│   ├── exercise_06_headers.py
│   ├── exercise_07_post_json.py
│   ├── exercise_08_timeout.py
│   ├── exercise_09_error_handling.py
│   ├── exercise_10_api_client_function.py
│   ├── exercise_11_save_api_data.py
│   └── exercise_12_api_report_generator.py
├── src/
│   └── api_client_lab/
│       ├── __init__.py
│       ├── client.py
│       ├── analyzer.py
│       ├── report.py
│       ├── writer.py
│       └── main.py
├── data/
│   └── output/
│       └── reports/
│           └── api_products_report.txt
├── requirements.txt
├── pyproject.toml
├── README.md
└── README_FR.md
```

## Package architecture

The final package is organized by responsibility:

```text
client.py   → handles API calls with requests
analyzer.py → analyzes product data
report.py   → builds the text report content
writer.py   → writes the report file with pathlib
main.py     → orchestrates the workflow
```

This structure keeps the code easier to read, test, maintain, and extend.

## Requirements

```text
Python 3.x
requests
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the final refactored package from the project root:

```bash
PYTHONPATH=src python -m api_client_lab.main
```

Expected terminal output:

```text
API products report generated:
data/output/reports/api_products_report.txt
```

## Generated report

The generated report contains:

```text
- total products available from the API
- number of products received
- limit and skip values
- average product price
- most expensive product
- product with the lowest stock
- formatted list of received products
```

Example report path:

```text
data/output/reports/api_products_report.txt
```

## Learning outcomes

This project validates the ability to:

```text
- consume an external API with Python
- use requests with params, headers, and timeout
- inspect HTTP status codes
- convert JSON responses into Python dictionaries
- process lists of dictionaries
- calculate simple business metrics
- generate a report from API data
- save files with pathlib
- structure Python code into modules
- separate responsibilities across a package
- run a package with python -m
```

## Status

The main learning module is complete.

Completed blocks:

```text
01 - HTTP basics
02 - First GET request
03 - HTTP status codes
04 - JSON response
05 - Query parameters
06 - Headers
07 - POST JSON
08 - Timeouts
09 - Error handling
10 - Reusable API client function
11 - Save API data
12 - API report generator mini-project
13 - Refactor into src package
```

## Possible next improvements

```text
- add unit tests
- add stronger error handling
- move API base URL into a configuration file
- support multiple product categories
- export reports as JSON or CSV
- package the project with pyproject.toml
```
