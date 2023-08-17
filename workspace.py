import requests
import json
from win10toast import ToastNotifier
import time

drops = 0
rises = 0
previous_price = ""
while True:
    t = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=gbp").text
    x = json.loads(t)

    price = str(x["bitcoin"]["gbp"])
    print(price)
    toast = ToastNotifier()

    if price < previous_price:
        drops += 1
        rises = 0
    elif price > previous_price:
        rises += 1
        drops = 0

    if drops >= 3:
        message = "Quick panic sell and make a loss! It was {} and now:".format(previous_price)
        toast.show_toast(message, price, duration=5)
    elif rises >= 3:
        message = "Buy, buy, buy while its more expensive! It was {} and now:".format(previous_price)
        toast.show_toast(message, price, duration=5)
    time.sleep(5)
    previous_price = price


