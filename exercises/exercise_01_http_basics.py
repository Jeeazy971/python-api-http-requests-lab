method = "GET"
protocol = "HTTPS"
domain = "api.foodguard.com"
resource = "products"
category = "fruits"
limit = 5
print("HTTP request analysis")
print()
print(f"Method: {method}")
print(f"Protocol: {protocol}")
print(f"Domain: {domain}")
print(f"Resource path: /{resource}")
print("Query parameters:")
print(f"- category = {category}")
print(f"- limit = {limit}")
print()
print("Meaning:")
print(f"The client asks the server to return a list of {resource} filtered by category {category}, limited to {limit} results.")
