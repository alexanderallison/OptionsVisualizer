from BinaryHeap import BinaryHeap


def calculate_stats_of_heap(heap):
    # initialize graph metrics
    results = {}  # dictionary of dictionaries, key = ticker, val = graph statistics(a dictionary)

    # process each option in the heap:
    while not heap.is_empty():
        option = heap.extract_min()  # grab first option
        ticker = option['ticker']
        if ticker not in results:
            results[ticker] = {
                'total_calls': 0,
                'total_puts': 0,
                'high_price': 0.0,
                'low_price': float('inf'),
                'expiration_dates': set()
            }
        if option['option_type'] == 'call' and option['volume'] is not None:
            results[ticker]['total_calls'] += option['volume']
        elif option['option_type'] == 'put' and option['volume'] is not None:
            results[ticker]['total_puts'] += option['volume']

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
        del results[ticker]['expiration_dates']  # only used to calculate date range so remove from results

    return results

