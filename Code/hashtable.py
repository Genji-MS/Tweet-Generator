#!python

from linkedlist import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        # Keep track of the number of initial buckets to prevent hard coding our hash EX. hash(key) % size
        self.size = init_size

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        √: Running time: O(n^2) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        √: Running time: O(n^2) Why and under what conditions?"""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values
        # √: Loop through all buckets
        # √: Collect all values in each bucket

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        √: Running time: O(n^2) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            if bucket.is_empty() == False:
                #not append, because the hash_table format will throw an error due to it's strict formatting 
                all_items+= (bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        √: Running time: O(n^2) if each of the buckets and linkedlist had to itterate over its entire length. Currently O(n) because linkedlist is optomized by storing and returning its length counter. Ideally storing a parameter and adjusting its value based on add/delete operations could make this an O(1) operation"""
        #STRETCH CHALLENGE: instead of counting each linkedlist item of buckets manually, we simply call the bucket.length function that is optomized by returning its stored length parameter
        count = 0
        for bucket in self.buckets:
            count += bucket.length()
        return count
        # √: Loop through all buckets
        # √: Count number of key-value entries in each bucket

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        √: Running time: O(n^2) Why and under what conditions?"""
        index = hash(key) % self.size
        item = self.buckets[index].find(lambda item: item[0] == key)
        return True if item != None else False
        # √: Find bucket where given key belongs
        # √: Check if key-value entry exists in bucket

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        √: Running time: O(n) Why and under what conditions?"""
        index = hash(key) % self.size
        item = self.buckets[index].find(lambda item: item[0] == key)
        if item != None:
            return item[1]
        else:
            raise KeyError(f'Key not found: {key}')
        # √: Find bucket where given key belongs
        # √: Check if key-value entry exists in bucket
        # √: If found, return value associated with given key
        # √: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        √: Running time: O(n) Why and under what conditions?"""
        index = hash(key) % self.size
        item = self.buckets[index].find(lambda item: item[0] == key)
        #'Update value' done by deleting the current tuple if it already exists
        if item != None:
            self.buckets[index].delete(item)
        new_item = (key, value)
        self.buckets[index].append(new_item)
        # √: Find bucket where given key belongs
        # √: Check if key-value entry exists in bucket
        # √: If found, update value associated with given key
        # √: Otherwise, insert given key-value entry into bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        √: Running time: O(n^2) running .delete requires us to parse the length of the linked list an additional time"""
        index = hash(key) % self.size
        item = self.buckets[index].find(lambda item: item[0] == key)
        if item != None:
            self.buckets[index].delete(item)
        else:
            raise KeyError(f'Key not found: {key}')
        # √: Find bucket where given key belongs
        # √: Check if key-value entry exists in bucket
        # √: If found, delete entry associated with given key
        # √: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    #inserted test ('X', 12) to see if overwriting a value works correctly 
    for key, value in [('I', 1), ('V', 5), ('X', 12), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
