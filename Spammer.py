import requests
import json
import time

def send_discord_message(webhook_url, message, num_times):
    payload = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        for _ in range(num_times):
            response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
            if response.status_code == 204:
                print("Message sent successfully!")
            else:
                print(f"Failed to send message. Status code: {response.status_code}")
            time.sleep(0.2)  # Sleep for 0.2 seconds between sends
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    webhook_url = input("Enter your Discord webhook URL: ")
    message = input("Enter the message you want to send: ")
    num_times = int(input("Enter the number of times to send the message: "))

    send_discord_message(webhook_url, message, num_times)
