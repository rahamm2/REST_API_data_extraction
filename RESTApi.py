# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 23:55:30 2021

@author: masoodhur
"""

import requests
import json

url="https://api.exchangeratesapi.io/latest?symbols=USD,GBP"
# Give connect to URL
response=requests.get(url)
print(response)
data=response.text
print(type(data))
parse=json.loads(data)
print(type(parse))
print(json.dumps(parse,indent=1))
# using parse you can extract data
date=parse['date']
print(date)

#Getting USD rate 
usd_rate=parse['rates']['USD']
print(usd_rate)

# GBP rate
GBP_rates=parse['rates']['GBP']
print(GBP_rates)

url1='https://api.exchangeratesapi.io/latest?base=USD'
response=requests.get(url1)
print(response)
data=response.text
print(type(data))
parse=json.loads(data)

rates=parse['rates']
print(rates)
#print(json.dumps(parse,indent=1))
for currency, rate in rates.items():
    print("1 USD=",currency,rate)