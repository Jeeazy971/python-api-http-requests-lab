status_code = 301

print("Status code analysis")
print()
print(f"Status code: {status_code}")

if 100 <= status_code < 200:
    print("Family: 1xx - Informational")
    print("Meaning: The server received the request and is continuing the process.")
elif 200 <= status_code < 300:
    print("Family: 2xx - Success")
    print("Meaning: The request was successfully processed.")
elif 300 <= status_code < 400:
    print("Family: 3xx - Redirection")
    print("Meaning: The client may need to follow another URL.")
elif 400 <= status_code < 500:
    print("Family: 4xx - Client error")
    print("Meaning: The request contains an error or the client is not allowed.")
elif 500 <= status_code < 600:
    print("Family: 5xx - Server error")
    print("Meaning: The server failed to process a valid request.")
else:
    print("Family: Unknown")
    print("Meaning: The status code does not match a standard HTTP family.")
