class MyHashMap:

    def __init__(self):
        self.HashMap = {}

    def put(self, key: int, value: int) -> None:
        self.HashMap[key] = value

    def get(self, key: int) -> int:
        if key in self.HashMap.keys():
            return self.HashMap[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.HashMap.keys():
            self.HashMap.pop(key)