from price import crypto_price
import requests

from datetime import date

BOT_TOKEN = "7795281162:AAEeYa2J23CnT1XwE_JhARdj3ZYisZKUOjQ"
CHAT_ID = "502712453"  # Use the group chat ID or user chat ID
MESSAGE = f"Егор станом на {date.today()} має {10} у профіті."

print(crypto_price())

def send_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("Message sent successfully!")
        return True
    else:
        print("Failed to send message. Error:", response.text)
        return False
    
    

def main():
    send_message(BOT_TOKEN, CHAT_ID, MESSAGE)

if __name__ == "__main__":
    main()