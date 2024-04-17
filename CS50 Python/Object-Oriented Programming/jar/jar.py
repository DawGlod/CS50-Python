class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Too many cookies added")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("You ate too many cookies")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity > 0:
            raise ValueError("Wrong value")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Not enough space")
        self._size = size


def main():
    jar = Jar(20, 10)
    jar.deposit(8)
    jar.withdraw(15)
    print(jar)



if __name__ == "__main__":
    main()
