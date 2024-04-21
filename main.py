import sys
from app import app
from dataFetch import *
from database.database import insertOptions, queryOptions
from HashTable import HashTable
from BinaryHeap import BinaryHeap
from helper import calculate_stats_of_heap


def setup_environment():
    print("Grabbing data from yahoo finance...")
    tickers = get_sp500_tickers()  # get tickers
    options_data = getOptionsData(tickers)  # get stock options data from all tickers and dates up to 100,000 points
    # print("Raw options data:", options_data[:5])  # Print the first few entries
    print("Got the data now inserting into database...")
    insertOptions(options_data)  # store them in SQL database table


def check_data_types(options_data):
    for index, option in enumerate(options_data):
        if not isinstance(option, dict):
            print(f"Item at index {index} is not a dictionary. Type: {type(option)}")
            print(f"Content: {option}")

    print("passed check_data_types")


def compute_Statistics():
    print("Computing statistics...")

    # get data from database
    options_data = queryOptions()
    # print("options data after queryOptions():", options_data[:5])  # Print the first few entries for testing

    check_data_types(options_data) # verify data is a list of dictionaries

    if len(sys.argv) > 1 and sys.argv[1] == 'heap':
        # if using BinaryHeap Class:
        print("using a binary heap...")

        # adjust key to sort by metric needed
        heap = BinaryHeap(key=lambda x: x['volume'] if x['volume'] is not None else float('inf'))
        for option in options_data:
            heap.insert(option)
        stats = calculate_stats_of_heap(heap)
        first_stock = next(iter(stats.items()))
        print(first_stock)
        print("Stats calculated using BinaryHeap")
    else:
        # if using HashTable Class:
        print("using a hash table...")
        ht = HashTable()
        for option in options_data:
            ht.insert(option['ticker'], option)
        stats = ht.calculate_stats()
        first_stock = next(iter(stats.items()))
        print(first_stock)
        print("Stats calculated using HashTable")

    return stats


def start_server():
    print("Starting server...")
    app.stats = compute_Statistics() # store stats in app
    app.run(debug=True)


if __name__ == '__main__':
    setup_environment()
    start_server()