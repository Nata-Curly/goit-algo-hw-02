from queue import Queue
import time
import random


queue = Queue()


def generate_request():
    """Створює нову заявку, додає заявку до черги"""
    request = random.randint(1, 1000)
    queue.put(request)
    print(f"Заявка {request} додана до черги 👌")


def process_request():
    """Обробяє заявку, видаляє заявку з черги"""
    if not queue.empty():
        request = queue.get()
        print(f"Заявка {request} обробляється ⌛")
    else:
        print("Черга пуста ❌")


def main():
    """Головний цикл програми"""
    while True:
        command = input("Введіть команду: ")
        if command == "вийти":
            break
        elif command == "згенеруй":
            generate_request()
            time.sleep(1)
        elif command == "оброби":
            process_request()
            time.sleep(1)


if __name__ == "__main__":
    main()
