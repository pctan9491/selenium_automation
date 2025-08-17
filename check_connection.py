import requests

try:
    response = requests.get("https://www.geeksforgeeks.org/", timeout=5)
    print(f"✅ Connection successful: {response.status_code}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    print("Using local test page instead...")