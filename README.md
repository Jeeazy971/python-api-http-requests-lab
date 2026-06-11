# Python API Client Lab

A progressive Python learning project focused on consuming HTTP APIs with `requests`, handling JSON responses, analyzing API data, generating local reports, and testing a small Python package with `pytest`.

The project starts with small isolated exercises and ends with a refactored API client package using a clean `src/` structure and a dedicated unit test suite.

## Project goals

This project was built to strengthen the fundamentals of API consumption in Python, then consolidate the code through modular architecture and unit testing.

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
- writing unit tests with pytest
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
- Test package behavior with pytest
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
├── tests/
│   ├── test_analyzer.py
│   ├── test_client.py
│   ├── test_report.py
│   └── test_writer.py
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
pytest
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

## Tests

The project includes a pytest test suite covering the main package responsibilities:

```text
test_analyzer.py → tests pure analysis functions, edge cases, parametrize, fixtures, and expected errors
test_report.py   → tests report text generation through important content assertions
test_writer.py   → tests file writing with tmp_path without polluting the real project folders
test_client.py   → tests API client behavior with monkeypatch without calling the real API
```

Run all tests from the project root:

```bash
PYTHONPATH=src pytest -q
```

For a detailed test report:

```bash
PYTHONPATH=src pytest
```

The current test suite validates:

```text
- happy paths
- edge cases
- missing-field errors with pytest.raises
- floating-point comparisons with pytest.approx
- repeated input cases with pytest.mark.parametrize
- reusable test data with pytest fixtures
- temporary file writing with tmp_path
- API behavior simulation with monkeypatch
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
- write useful unit tests with pytest
- test pure functions, file writing, report generation, and API client behavior
- isolate external dependencies in tests with monkeypatch
```

## Status

The main API learning module and the pytest mini-module are complete.

Completed API blocks:

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

Completed pytest blocks:

```text
01 - First unit tests with pytest
02 - Edge cases and expected errors
03 - Parametrized tests with pytest.mark.parametrize
04 - Fixtures with pytest.fixture
05 - Report generation unit test
06 - File writer test with tmp_path
07 - API client tests with monkeypatch
08 - Test suite consolidation and README documentation
```

## Possible next improvements

```text
- add stronger API error handling
- move the API base URL into a configuration file
- support multiple product categories
- export reports as JSON or CSV
- add GitHub Actions to run pytest automatically
- add test coverage reporting
- package the project more fully with pyproject.toml
```
