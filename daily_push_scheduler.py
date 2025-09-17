import requests
import schedule
import time
from datetime import datetime
import os

# API endpoint
API_URL = "https://dailybrief-ai.onrender.com/dailybrief"

# Log file path
LOG_FILE = "daily_push_log.txt"

# Notification function
def send_push_notification():
    params = {
        "title": "Your Notification Title",
        "message": "This is the body of your push notification",
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        log_message = f"{datetime.now()}: Notification sent successfully. Response: {response.text}\n"
        print(log_message)
    except requests.exceptions.RequestException as e:
        log_message = f"{datetime.now()}: Error sending notification: {e}\n"
        print(log_message)
    
    # Append log to file
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_message)

# Schedule daily notification (change time as needed)
schedule.every().day.at("07:00").do(send_push_notification)

# Send notification immediately on script start
send_push_notification()

print("Scheduler started. Waiting for the scheduled time...")

# Run scheduler continuously
while True:
    schedule.run_pending()
    time.sleep(30)  # Check every 30 seconds
