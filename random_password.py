# Рандомный пароль вида: skREpBgKVb9IM3KomGrxqccKRhWHgGywdOA99aEAZh

from string import ascii_letters, digits
import random


def generate_password(size=48):
    """ Создание рандомного пароля определенной длины из букв и цифр.
    """
    chars = ascii_letters + digits    # ascii_letters: a-z + A-Z, digits: 0-9.

    password = ''.join(random.choice(chars) for x in range(size))
    
    return password



print(generate_password(42))
