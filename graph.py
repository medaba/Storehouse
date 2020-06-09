# Поиск "в ширину"

from collections import deque

graph = {}

graph["cab"] = ["gad"]
graph["gad"] = ["car", "cat"]
graph["car"] = ["cat", "bar"]
graph["bar"] = ["bat"]
graph["cat"] = ["mat", "bat"]
graph["mat"] = []
graph["bat"] = ["pen"]
graph["pen"] = []


def breadth_first_search(graph, start, destination):
    search_queue = deque()        # создание очереди поиска

    search_queue += graph[start] # добавление всех соседей стартового узла в очередь поиска

    searched = []                 # в этот список будут добавляться уже проверенные э-ты

    while search_queue:                # пока очередь не пуста
        point = search_queue.popleft() # получение эл-та c левого края очереди
        
        if not point in searched:
            print(f"Проверяется узел: {point}")
            
            if destination in graph[point]:
                print("Путь найден")
                return True
            else:
                # иначе все соседи добавляются в список очереди
                search_queue += graph[point]
                searched.append(point) # добавление провереных узлов в список
            
    return False # если выполнение кода дошло до этой строки, значит ничего не найдено
       
       
breadth_first_search(graph, "cab", "pen") # пытаемся найти "путь" от узла "cab" до "pen"