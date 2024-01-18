class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        if type(self.capacity) != int or self.capacity < 0:
            raise ValueError

    def __str__(self):
        return "'🍪'*self.capacity"

    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError

    def withdraw(self, n):
        self.size -= n
        if self.size < self.capacity:
            raise ValueError

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.size

def main():
    a= Jar(-12)
    print(a)
    # Input =

if __name__ == "__main":
    main()
