# OptionsVisualizer
Python webapp that visualizes options data using a bubble chart

Here is a diagram of the layout: 

/OptionsVisualizer<br>
│<br>
├── app.py # Main application file where Flask app is initialized<br>
│<br>
├── data_fetching # Module for data fetching functionalities<br>
│ ├── init.py<br>
│ ├── dataFetch.py # Functions to fetch market data<br>
│ ├── sp500_tickers.py # Functions to fetch S&P 500 tickers<br>
│ <br>
├── database # Database interaction module<br>
│ ├── init.py<br>
│ ├── models.py # Database models<br>
│ ├── database.py # Database connection and session management<br>
│ <br>
├── data_structures # Data structures for in-memory processing<br>
│ ├── init.py<br>
│ ├── HashTable.py # Hash table operations<br>
│ <br>
├── templates # Flask templates<br>
│ ├── index.html<br>
│ ├── chart.html<br>
│ <br>
├── static # Static files like CSS, JS<br>
│ ├── css<br>
│ ├── js<br>
│ <br>
├── tests # Test suite for the application<br>
│ ├── init.py<br>
│ ├── test_data_fetching.py<br>
│ ├── test_database.py<br>
│ ├── test_data_structures.py<br>

**To setup:**

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Note: in pycharm use a venv interpreter

**Install libs:** 

pip install flask yfinance plotly pandas sqlalchemy pandas_datareader setuptools yfinance[nospam]

**to run:**

python main.py 
after stats calculated go to to view Bubble chart:
http://127.0.0.1:5000/chart

<u>** Note: on initial run will take 5-10 min for database to build **</u>
Has a limit on API calls that shouldn't be spammed. 
