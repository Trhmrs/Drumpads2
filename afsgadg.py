import os
import sys
import pyttsx3
import requests
from forex_python.converter import CurrencyRates
c=CurrencyRates()
api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
appid = ''
r = requests.get(url=api_url, params=dict(q='Anderson', APPID=appid))
print("%.2f" %(c.convert('USD', 'RUB', r.json()['bpi']['USD']['rate_float'])))
engine=pyttsx3.init()
engine.say("%.2f" %(c.convert('USD', 'RUB', r.json()['bpi']['USD']['rate_float'])))
engine.runAndWait()
