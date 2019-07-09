import threading, time, random

class Singleton:
    _instance, _lock = None, threading.Lock()
    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

def task():
    time.sleep(random.random())
    print(Singleton())

if __name__ == '__main__':
    for _ in range(5):
        threading.Thread(target=task).start()
