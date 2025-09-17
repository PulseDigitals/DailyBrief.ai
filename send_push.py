import requests

API_URL = "https://dailybrief-ai.onrender.com/dailybrief"

params = {
    "title": "Your Notification Title",
    "message": "This is the body of your push notification",
}

try:
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    print("Push notification triggered successfully!")
    print("Response text:", response.text)  # Use .text instead of .json()
except requests.exceptions.RequestException as e:
    print("Error sending push notification:", e)

