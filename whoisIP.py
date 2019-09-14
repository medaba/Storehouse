#!/usr/bin/env python3

# Получение информации об IP либо Домене.

import requests
from whois import whois
from pprint import pprint

def get_ip():
    """
    Делает запрос к "api.ipify.org" и возвращает ваш текущий IP.
    """
    r = requests.get('https://api.ipify.org?format=json')
    
    if r.ok:
        ip = r.json()["ip"]
        return ip
    else:
        return r.status_code

def whois_ip(ip):
    """
    Аналог сервиса 'whois'.
    Получение открытой информации об IP либо домене.    
    """
    w = whois(ip)
    return {"ip/domain": ip, "whois": w}


if __name__ == '__main__':
    try:
        print(get_ip())
        pprint(whois_ip("https://pythonanywhere.com/"))
    except Exception as error:
        print("Error:", error, "\nType:", type(error))

    