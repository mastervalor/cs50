class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("This is not a non-negative number")
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if self.cookies + n > self._capacity:
            raise ValueError("Cannot deposit more cookies than the jar's capacity.")
        self.cookies += n

    def withdraw(self, n):
        if n > self.cookies:
            raise ValueError("Cannot deposit more cookies than the jar's capacity.")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies


jar = Jar()
print(str(jar.capacity))
jar.deposit(2)
print(str(jar))
