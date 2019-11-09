from Hash_tables import ChainedHashTable, OpenAddressHashTable
from Hash_functions import HashFunctionDivide, HashFunctionMultiply,\
    HashFunctionOpenLinear, HashFunctionOpenQuadratic, HashFunctionOpenDouble


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
            self.__hash_table = OpenAddressHashTable(values, HashFunctionOpenDouble(len(values)))

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
