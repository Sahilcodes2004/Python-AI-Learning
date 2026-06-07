import requests

response = requests.get("https://api.github.com")

data = response.json()

print("Status:", response.status_code)
print("Repository URL:", data["current_user_url"])