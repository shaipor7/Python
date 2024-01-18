class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        if type(self.capacity) != int or self.capacity < 0:
            raise ValueError

    def __str__(self):
        return 🍪*capacity

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

def main():
    Input =

if __name__ == "__main":
    main()
