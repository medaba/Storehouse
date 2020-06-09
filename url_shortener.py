# Укорачиватели ссылок

import requests
from pyshorteners import Shortener, Shorteners


def short_link(link, shortener_name="TINYURL"):
    """
    Укорачиватель ссылок - pyshorteners

    :param link: Ссылка, которую нужно сократить.
    :param shortener_name: имя сервиса для укорачивания ссылок

    Доступные сервисы: TINYURL, ISGD, DAGD, CLCKRU, CHILPIT
    """
    shortener = getattr(Shorteners, shortener_name)
    s = Shortener(shortener)
    short_link = s.short(link)
    return short_link


def relink(link):
    """
    Получение сокращенного URL через requests обращение к
    API https://rel.ink/
    """
    main_url = 'https://rel.ink/'
    api_url = main_url + 'api/links/'
    r = requests.post(api_url, {'url': link}).json()
    hash_id = r['hashid']
    short_link = main_url + hash_id

    return short_link



if __name__ == '__main__':
    print(short_link('https://google.com', 'CLCKRU'))
    
    
