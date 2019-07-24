# Бесконечная карусель функций

from collections import deque
from time import sleep


def first():
    print("First Function")

def second():
    print("Second Function")

def third():
    print("Third Function")

lst = [first, second, third]


def queue_loop(lst, pause=1):
    """Принимает список функций,
       достает их по одной из списка, 
       запускает и отправляет в конец очереди.
       """
    queue = deque(lst)             # Создаем очередь из переданного списка ф-й. 
    loop = True

    while loop:
        current = queue.popleft()  # Достаем ф-ю из начала очереди
        current()                  # Исполняем ее
        queue.append(current)      # Добавляем отработавшую ф-ю в конец очереди
        sleep(pause)               # Спим 1сек и повторяем
        

if __name__ == '__main__':

    queue_loop(lst)
