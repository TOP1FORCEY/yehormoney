from pytz import timezone
import requests, time, datetime

def crypto_price():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd"
    price = requests.get(url)
    data = price.json()

    return round((data["dogecoin"]["usd"] - 0.37129) * 2000, 3)


dt = datetime.datetime.now(tz = timezone("Europe/Kyiv"))
now = dt.strftime('%X %A %m/%d/%Y')

translate = {"Monday": "Понеділок", "Tuesday": "Вівторок", "Wednesday": "Середу", "Thursday": "Четверг", "Friday": "П'ятницю", "Saturday": "Субботу", "Sunday": "Неділю",}

for key in translate.keys():
    now = now.replace(key, translate[key])

BOT_TOKEN = "7795281162:AAEeYa2J23CnT1XwE_JhARdj3ZYisZKUOjQ"
CHAT_ID = "502712453"  # Use the group chat ID or user chat ID
if crypto_price() > 0:
    MESSAGE = f"Егор о {now.split(" ")[0].split(":")[0]}:{now.split(" ")[0].split(":")[1]} у {now.split(" ")[1]} {now.split(" ")[2]} заробив {crypto_price()} USD."
else:
    MESSAGE = f"Егор о {now.split(" ")[0].split(":")[0]}:{now.split(" ")[0].split(":")[1]} у {now.split(" ")[1]} {now.split(" ")[2]} проєбав {crypto_price()} USD."

def send_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print(f"Message ({MESSAGE}) sent successfully!")
        return True
    else:
        print("Failed to send message. Error:", response.text)
        return False

def main():
    while True:
        send_message(BOT_TOKEN, CHAT_ID, MESSAGE)
        time.sleep(21600)

if __name__ == "__main__":
    main()