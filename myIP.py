#!/usr/bin/env python3

# Делает запрос к "api.ipify.org" и возвращает ваш текущий IP.

import requests
import whois
from pprint import pprint

def get_ip():
    r = requests.get('https://api.ipify.org?format=json')
    
    if r.ok:
        ip = r.json()["ip"]
        return ip
    else:
        return r.status_code

def who_am_i(ip):
    print(ip)
    w = whois.whois('77.106.112.231')
    pprint(w)


if __name__ == '__main__':
    try:
        my_ip = get_ip()
        who_am_i(my_ip)
    except Exception as error:
        print("Error:", error, "\nType:", type(error))


