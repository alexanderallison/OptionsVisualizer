import unittest


class BinaryHeap:
    def __init__(self, key=lambda x: x):
        self.heap = []
        self.key = key

    def insert(self, item):
        # Inserts new item into heap.
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        # Removes and returns smallest item from heap.
        if not self.heap:
            raise IndexError("extract_min() called on empty heap")
        self._swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()
        if self.heap:
            self._bubble_down(0)
        return min_item

    def _bubble_up(self, index):
        # Pushes up item at provided index to correct position in heap.
        parent_index = (index - 1) // 2
        while index > 0 and self.key(self.heap[index]) < self.key(self.heap[parent_index]):
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def _bubble_down(self, index):
        # Pushes down item at provided index to correct position in heap.
        child_index = 2 * index + 1
        while child_index < len(self.heap):
            right_child_index = child_index + 1
            if (right_child_index < len(self.heap) and
                    self.key(self.heap[right_child_index]) < self.key(self.heap[child_index])):
                child_index = right_child_index

            if self.key(self.heap[child_index]) >= self.key(self.heap[index]):
                break

            self._swap(child_index, index)
            index = child_index
            child_index = 2 * index + 1

    def _swap(self, i, j):
        # Swaps elements at provided indices.
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def peek(self):
        # Returns smallest item without removing it.
        if not self.heap:
            raise IndexError("peek() called on empty heap")
        return self.heap[0]

    def size(self):
        # Returns number of items in heap.
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


"""
#TESTING
class TestBinaryHeap(unittest.TestCase):
    def test_Heap(self):
        # initialize heap with key to sort by 'volume'
        heap = BinaryHeap(key=lambda x: x['volume'])
        test_data = [
    {'ticker': 'MMM', 'option_type': 'call', 'strike': 75.0, 'expiration': '2024-04-26', 'volume': 1.0},
    {'ticker': 'MMM', 'option_type': 'call', 'strike': 80.0, 'expiration': '2024-04-26', 'volume': 50.0},
    {'ticker': 'MMM', 'option_type': 'call', 'strike': 83.0, 'expiration': '2024-04-26', 'volume': 2.0},
    {'ticker': 'MMM', 'option_type': 'call', 'strike': 87.0, 'expiration': '2024-04-26', 'volume': 3.0},
    {'ticker': 'MMM', 'option_type': 'call', 'strike': 88.0, 'expiration': '2024-04-26', 'volume': 2.0}
]
        # insert all options data into the heap
        for data in test_data:
            heap.insert(data)
        # initialize graph metrics
        results = {} # dictionary

        # process each option in the heap:
        while not heap.is_empty():
            option = heap.extract_min() # grab first option
            ticker = option['ticker']
            if ticker not in results:
                results[ticker] = {
                    'total_calls': 0,
                    'total_puts': 0,
                    'high_price': 0.0,
                    'low_price': float('inf'),
                    'expiration_dates': set()
                }
            if option['option_type'] == 'call':
                results[ticker]['total_calls'] += 1
            else:
                results[ticker]['total_puts'] += 1

            results[ticker]['high_price'] = max(results[ticker]['high_price'], option['strike'])
            results[ticker]['low_price'] = min(results[ticker]['low_price'], option['strike'])
            results[ticker]['expiration_dates'].add(option['expiration'])

        for ticker, stats in results.items():
            sorted_dates = sorted(stats['expiration_dates'])
            date_range = (sorted_dates[0], sorted_dates[-1]) if sorted_dates else (None, None)
            total_options = stats['total_calls'] + stats['total_puts']
            call_put_ratio = stats['total_calls'] / stats['total_puts'] if stats['total_puts'] > 0 else -1
            results[ticker].update({
                'total_options': total_options,
                'call_put_ratio': call_put_ratio,
                'date_range': date_range
            })
            del results[ticker]['expiration_dates'] # only used to calculate date range

        self.assertEqual(results['MMM']['total_calls'], 5)
        self.assertEqual(results['MMM']['total_puts'], 0)
        self.assertEqual(results['MMM']['high_price'], 88.0)
        self.assertEqual(results['MMM']['low_price'], 75.0)
        self.assertEqual(results['MMM']['date_range'], ('2024-04-26', '2024-04-26'))

        print_results(self, results)
def print_results(self, results):
    for ticker, stats in results.items():
        print(f'Stats for {ticker}:')
        for key, value in stats.items():
            print(f'\t{key}: {value}')
        print()

if __name__ == '__main__':
    unittest.main()

"""