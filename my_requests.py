import requests

def retry_request(url, max_retries=3):
    for _ in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Check for HTTP errors
            return response
        except (requests.RequestException, TimeoutError):
            pass
    return None  # Return None if all retries fail

response = retry_request('https://example.com')
