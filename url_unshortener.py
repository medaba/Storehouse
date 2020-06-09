# "Дешифратор" коротких ссылок

from unshortenit import UnshortenIt


def url_unshortener(short_link):
	"""
    Расшифровка коротких ссылок

    :param shor_link: короткая ссылка, которую нужно расшифровать.
    :return: возвращает оригинульную ссылку.

    Умеет расшифровывать 300+ сервисов-укорачивателей
    """
	unshortener = UnshortenIt()
	original_url = unshortener.unshorten(short_link)
	return original_url


url = url_unshortener("http://tinyurl.com/mbq3m")

print(url)
