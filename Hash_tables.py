from Linked_list import LinkedList


class HashTableInterface:
    def insert(self, value):
        raise NotImplemented

    def delete(self, value):
        raise NotImplemented

    def search(self, value):
        raise NotImplemented


class OpenAddressHashTable(HashTableInterface):
    def __init__(self, values, hash_func_obj):
        self.values = values
        self.size = hash_func_obj.get_size()
        self.hash_func = hash_func_obj.open_hash
        self.table = [None for _ in range(self.size)]
        self.deleted = [False for _ in range(self.size)]
        self.__collisions_amount = 0

        for value in values:
            self.insert(value)

    def insert(self, value):
        i = 0
        while i < self.size:
            j = self.hash_func(value, i)
            if self.table[j] is None or self.deleted[j]:
                self.table[j] = value
                self.deleted[j] = False
                return j
            i += 1
            self.__collisions_amount += 1
        return -1

    def delete(self, value):
        i = 0
        while i < self.size:
            j = self.hash_func(value, i)
            if self.table[j] == value:
                self.deleted[j] = True
                return j
            i += 1
            if self.table[j] is None or self.deleted[j]:
                return -1
        return -1

    def search(self, value):
        i = 0
        while i < self.size:
            j = self.hash_func(value, i)
            if self.table[j] == value and not self.deleted[j]:
                return 1
            i += 1
            if self.table[j] is None or self.deleted[j]:
                return 0
        return 0

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