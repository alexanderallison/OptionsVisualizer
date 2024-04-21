from flask import Flask, jsonify, render_template, request
import os
import time
from BinaryHeap import BinaryHeap
from HashTable import HashTable

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to Team 144 ? I think the Flask server is running."
    
@app.route('/chart')
def chart():
    return render_template('chart.html', time_elapsed=app.time_elapsed)
    
@app.route('/api/options-data', methods=['GET'])
def get_all_options_data():
    # return stats stored in app
    return jsonify(app.stats)

       # return jsonify({'error': 'Statistics not available'}), 500

@app.route('/api')
def test():
    print("hello")

@app.route('/insert', methods=['POST'])
def insert_data():
    option = request.json
    start_time = time.time()
    data_structure.insert(option)
    end_time = time.time()
    return jsonify({'status': 'success', 'time_taken': f"{end_time - start_time:.5f} seconds"}), 200

@app.route('/get', methods=['GET'])
def get_data():
    start_time = time.time()
    if isinstance(data_structure, HashTable):
        key = request.args.get('key')
        data = data_structure.get(key)
    else:
        data = data_structure.extract_min() if data_structure.size() > 0 else None
    end_time = time.time()
    if data is not None:
        return jsonify({'data': data, 'time_taken': f"{end_time - start_time:.5f} seconds"}), 200
    else:
        return jsonify({'error': 'Data not found', 'time_taken': f"{end_time - start_time:.5f} seconds"}), 404

if __name__ == '__main__':
    app.run(debug=True)
