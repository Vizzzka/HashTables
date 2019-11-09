import math


# pre processing
resheto = [True for _ in range(200009 + 5)]

primes_numbers = []
for i in range(2, len(resheto)):
    if resheto[i]:
        primes_numbers.append(i)
        for j in range(2 * i, len(resheto), i):
            resheto[j] = False


class HashFunctionDivide:

    def __init__(self, n):
        self.n = n
        self.m = self.count_size()

    def count_size(self):
        primes = primes_numbers
        for p in primes:
            if p > self.n * 3:
                break
            if p > self.n:
                res = p

        return res

    def get_size(self):
        return self.m

    def hash(self, x):
        return x % self.m


class HashFunctionMultiply:
    A = (math.sqrt(5) - 1) / 2

    def __init__(self, n):
        self.n = n
        self.m = self.count_size()

    def count_size(self):
        res = 1
        while res <= self.n:
            res *= 2
        return res

    def get_size(self):
        return self.m

    def hash(self, x):
        return int((x * self.A - int(x * self.A)) * self.m)


class HashFunctionOpenLinear(HashFunctionMultiply):

    def open_hash(self, x, i):
        return (self.hash(x) + i) % self.m


class HashFunctionOpenQuadratic(HashFunctionMultiply):

    c1 = 0
    c2 = 1

    def open_hash(self, x, i):
        return (self.hash(x) + self.c1 * i + self.c2 * i * i) % self.m


class HashFunctionOpenDouble(HashFunctionDivide):
    def hash2(self, x):
        return 1 + x % (self.m - 1)

    def open_hash(self, x, i):
        return (self.hash(x) + self.hash2(x) * i) % self.m

