#!/usr/bin/env python3

# Делает запрос к "api.ipify.org" и возвращает ваш текущий IP.

import requests

def get_ip():
    r = requests.get('https://api.ipify.org?format=json')
    
    if r.ok:
        ip = r.json()["ip"]
        return ip
    else:
        return r.status_code

if __name__ == '__main__':
    try:
        print(get_ip())
    except Exception as error:
        print("Error:", error, "\nType:", type(error))