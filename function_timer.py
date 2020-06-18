# -*- coding: utf-8 -*-

import time


def func_timer(func):
    """Декоратор для вычисления времени отрабатывания принятой ф-и
    """
    start_time = time.time()

    def new_func():
        func()
        print(f"--- {time.time() - start_time} seconds ---")

    return new_func



if __name__ == "__main__":
    # Пример использования

    @func_timer
    def some_func():
        for i in range(20):
            print(i)


    some_func()
