import unittest


class HashTable:
    def __init__(self, size=1000):
        # initialize hash table with empty buckets
        self.size = size
        self.table = [[] for i in range(self.size)]  # lists of lists [ [key0, val0], [key1, val1] ... ]
        self.count = 0

    def _hash(self, key):
        # hash function using built in python hash() function to minimize collisions
        # determines the index / bucket to put data in
        return hash(key) % len(self.table)

    def insert(self, key, val):

        # check load factor and resize if met or exceeded
        if self.count / self.size >= 0.7:
            self._resize(2 * self.size)

        # inserts a key, val pair into the hash table
        index = self._hash(key)
        bucket = self.table[index]

        if val['volume'] is None:
            val['volume'] = 0

        for item in bucket:
            if item[0] == key:  # if key exists, update the val
                if not isinstance(item[1], list):
                    item[1] = [item[1]]  # convert to list if its not
                item[1].append(val)  # append to list
                return

        bucket.append((key, [val]))
        # if key doesn't exist add it to end of the bucket
        self.count += 1

    def get(self, key):
        # get the val associated with key, return none if not found
        index = self._hash(key)
        bucket = self.table[index]
        for item in bucket:
            if item[0] == key:
                return item[1]
        return None

    def remove(self, key):
        # removes an element with the associated key from the hash table
        index = self._hash(key)
        bucket = self.table[index]
        for i, item in enumerate(bucket):
            if item[0] == key:  # if we find the key in the bucket, delete the list with that key from the bucket
                del bucket[i]
                self.count -= 1
                return

    def _resize(self, newSize):
        # initialize a new hash table with target size
        oldTable = self.table
        self.size = newSize
        self.table = [[] for i in range(self.size)]
        self.count = 0

        for bucket in oldTable:
            for key, val in bucket:
                self.insert(key, val)  # rehash and insert values from old table into new table

    def calculate_stats(self):
        results = {}
        for bucket in self.table:
            for key, options in bucket:
                """ DEBUG STUFF
                # Check each option individually instead of using all() for better error reporting
                valid_options = []
                for option in options:
                   if isinstance(option, dict):
                       valid_options.append(option)
                    else:
                        print(f"Error: Item is not a dictionary for key {key}. Item: {option}")

                if len(valid_options) != len(options):
                    print(f"Error: Not all items in options are dictionaries for key {key}. Skipping this key.")
                    continue  # Skip this key if validation fails
                print(valid_options) DEBUG
                """

                total_calls = sum(option['volume'] for option in options if option['option_type'] == 'call'
                                  and option['volume'] is not None)
                total_puts = sum(option['volume'] for option in options if option['option_type'] == 'put'
                                 and option['volume'] is not None)
                total_options = total_calls + total_puts

                call_put_ratio = total_calls / total_puts if total_options > 0 else -1

                try:
                    high_price = max(option['strike'] for option in options)
                    low_price = min(option['strike'] for option in options)
                    expiration_dates = {option['expiration'] for option in options}
                    sorted_dates = sorted(expiration_dates) if expiration_dates else None

                    date_range = (sorted_dates[0], sorted_dates[-1]) if sorted_dates else (None, None)
                except ValueError as e:
                    print(f"Error: unexpected value: {e}")
                    high_price, low_price = None, None
                    date_range = (None, None)

                results[key] = {
                    'total_calls': total_calls,
                    'total_puts': total_puts,
                    'total_options': total_options,
                    'call_put_ratio': call_put_ratio,
                    'high_price': high_price,
                    'low_price': low_price,
                    'date_range': date_range
                }
        return results

"""
#for testing:
ht = HashTable()
ht.insert('AAPL', {'option_type': 'call', 'strike': 150, 'expiration': '2023-12-15','volume': 1.0})
ht.insert('AAPL', {'option_type': 'call', 'strike': 150, 'expiration': '2023-12-15','volume': 50.0})
ht.insert('AAPL', {'option_type': 'put', 'strike': 145, 'expiration': '2023-12-15','volume': 2.0})
ht.insert('GOOG', {'option_type': 'call', 'strike': 1500, 'expiration': '2023-12-15','volume': 3.0})
ht.insert('GOOG', {'option_type': 'put', 'strike': 1480, 'expiration': '2023-12-15','volume': 5.0})
stats = ht.calculate_stats()
print(stats) 
#output stats = dictionary of dictionaries
# {'AAPL': {'total_calls': 51.0, 'total_puts': 2.0, 'total_options': 53.0, 'call_put_ratio': 25.5, 'high_price': 150, 'low_price': 145, 'date_range': (('2023-12-15', '2023-12-15'), None)}, 
# 'GOOG': {'total_calls': 3.0, 'total_puts': 5.0, 'total_options': 8.0, 'call_put_ratio': 0.6, 'high_price': 1500, 'low_price': 1480, 'date_range': (('2023-12-15', '2023-12-15'), None)}}


class TestHashTable(unittest.TestCase):
    def test_insert_retrieve(self):
        ht = HashTable()
        test_data = {'ticker': 'MMM', 'option_type': 'call'}
        ht.insert('MMM', test_data)
        retrieved = ht.get('MMM')
        self.assertEqual(retrieved, [test_data])  # expecting a list containing the dictionary
        self.assertIsInstance(retrieved, list)
        self.assertTrue(all(isinstance(entry, dict) for entry in retrieved))

class TestVolumeHandling(unittest.TestCase):
    def test_volume_none(self):
        ht = HashTable()
        ht.insert('AAPL', {'option_type': 'call', 'volume': None})
        self.assertEqual(ht.calculate_stats()['AAPL']['total_calls'], 0)  # expecting 0 because None should be treated as 0

if __name__ == '__main__':
    unittest.main()
"""