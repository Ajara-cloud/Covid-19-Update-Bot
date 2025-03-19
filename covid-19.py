import requests
from win10toast import ToastNotifier
import json
import time


def update():
    r = requests.get(' https://disease.sh/v3/covid-19/all')
    data = r.json()
    text = f'Confirmed Cases: {data['cases']}\nDeaths: {data['deaths']}\nRecovered: {data['recovered']}'

    while True:
        toast = ToastNotifier()
        toast.show_toast('Covid-19 Updates', text, duration=10)
        time.sleep(60 * 60)

update()