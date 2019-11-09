import math


resheto = [True for _ in range(100000 + 5)]

primes_numbers = []
for i in range(2, len(resheto)):
    if resheto[i]:
        primes_numbers.append(i)
        for j in range(2 * i, len(resheto), i):
            resheto[j] = False


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def add(self, value):
        self.size += 1
        if not self.head:
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
            self.head.next.prev = self.head

    def search(self, value):
        prob = self.head
        col = 0
        while prob:
            if prob.value == value:
                col += 1
            prob = prob.next
        return col

    def delete(self, value):
        self.size -= 1
        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = None

        prob = self.head
        while prob:
            if prob.value == value:
                prob.prev.next = prob.next
                prob.next.prev = prob.prev
                return True
            prob = prob.next

        return False


class HashTableInterface:
    def insert(self, value):
        raise NotImplemented

    def delete(self, value):
        raise NotImplemented

    def search(self, value):
        raise NotImplemented


class HashFunctionDivide:

    def __init__(self, n):
        self.n = n
        self.m = self.count_size()

    def count_size(self):
        primes = primes_numbers
        for p in primes:
            if p > self.n:
                return p

    def get_size(self):
        return self.m

    def hash(self, x):
        return x % self.m


class HashFunctionMultiply:

    def __init__(self, n):
        self.n = n
        self.m = self.count_size()
        self.A = (math.sqrt(5) - 1) / 2

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


class OpenAddressHashTable(HashTableInterface):
    def __init__(self, values, hash_func_obj):
        self.values = values
        self.size = hash_func_obj.get_size()
        self.hash_func = hash_func_obj.open_hash
        self.table = [None for _ in range(self.size)]
        self.__collisions_amount = 0

        for value in values:
            self.insert(value)

    def insert(self, value):
        i = 0
        while i < self.size:
            j = self.hash_func(value, i)
            if not self.table[j]:
                self.table[j] = value
                return j
            i += 1
            self.__collisions_amount += 1
        return -1

    def delete(self, value):
        i = 0
        while i < self.size:
            j = self.hash_func(value, i)
            if self.table[j] == value:
                self.table[j] = None
                return j
            i += 1
        return -1

    def search(self, value):
        i = 0
        col = 0
        while i < self.size:
            j = self.hash_func(value, i)
            if self.table[j] == value:
                col += 1
            i += 1
        return col

    def get_collisions_amount(self):
        return self.__collisions_amount


class ChainedHashTable(HashTableInterface):
    def __init__(self, values, hash_function_obj):
        self.values = values
        self.size = hash_function_obj.get_size()
        self.hash_func = hash_function_obj.hash
        self.table = [LinkedList() for i in range(self.size)]
        self.__collisions_amount = 0

        for value in values:
            self.insert(value)

    def insert(self, value):
        key = self.hash_func(value)
        if self.table[key].size:
            self.__collisions_amount += 1
        self.table[key].add(value)

    def search(self, value):
        key = self.hash_func(value)
        return self.table[key].search(value)

    def delete(self, value):
        key = self.hash_func(value)
        return self.table[key].delete(value)

    def get_collisions_amount(self):
        return self.__collisions_amount


class HashTable:
    types = ["Chained hash table with division method",
             "Chained hash table with multiplication method",
             "Open hash table with linear method",
             "Open hash table with quadratic method",
             "Open hash table with double method"]

    def __init__(self, hash_type, values):
        self.hash_type = self.types[hash_type - 1]
        if hash_type == 1:
            self.__hash_table = ChainedHashTable(values, HashFunctionDivide(len(values)))
        if hash_type == 2:
            self.__hash_table = ChainedHashTable(values, HashFunctionMultiply(len(values)))
        if hash_type == 3:
            self.__hash_table = OpenAddressHashTable(values, HashFunctionOpenLinear(len(values)))
        if hash_type == 4:
            self.__hash_table = OpenAddressHashTable(values, HashFunctionOpenQuadratic(len(values)))
        if hash_type == 5:
            self.__hash_table = OpenAddressHashTable(values, HashFunctionOpenQuadratic(len(values)))

    def get_collisions_amount(self):
        return self.__hash_table.get_collisions_amount()

    def find_sum(self, s):
        for value in self.__hash_table.values:
            value2 = s - value
            # if sum consists of two equal values
            if value == value2:
                if self.__hash_table.search(value) > 1:
                    return value, value2
                continue

            # if sum consists of two different values
            if self.__hash_table.search(value2):
                return value, value2
        return None


if __name__ == "__main__":
    ex = HashTable(5, [2, 4, 4, 5, 10, 17])
    print(ex.get_collisions_amount())
    print(ex.find_sum(8))
