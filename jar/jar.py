class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪'*self.capacity

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
        return self._capacity

    @capacity.setter
    def capacity(self, cap_cookie):
        if type(cap_cookie) != int or cap_cookie < 0:
            raise ValueError
        self._capacity = cap_cookie

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, cookie):
        if cookie > self.capacity or cookie < 0 :
            raise ValueError
        self._size = cookie


def main():
    a= Jar(0)
    print(a)
    # Input =

if __name__ == "__main__":
    main()
