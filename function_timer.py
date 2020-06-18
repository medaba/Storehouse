# -*- coding: utf-8 -*-

import time


def func_timer(func):
    """Декоратор для вычисления времени отрабатывания принятой ф-и
    """
    def new_func():
        start_time = time.time()
        func()
        print(f"--- {time.time() - start_time} seconds ---")

    return new_func



def func_timer2(run, coro):
    """Вариант таймера для асинхронных функций

       Пример использования:
       func_timer2(asyncio.run, main)
    """
    start_time = time.time()
    run(coro())
    print(f"--- {time.time() - start_time} seconds ---")


if __name__ == "__main__":
    # Пример использования

    @func_timer
    def some_func():
        for i in range(20):
            print(i)


    some_func()
