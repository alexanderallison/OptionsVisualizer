# OptionsVisualizer
Python webapp that visualizes options data using a bubble chart

Here is a diagram of the layout: 

/OptionsVisualizer<br>
│<br>
├── app.py # Main application file where Flask app is initialized<br>
│<br>
├── data_fetching # Module for data fetching functionalities<br>
│ ├── dataFetch.py # Functions to fetch market data<br>
│ <br>
├── database # Database interaction module<br>
│ ├── init.py<br>
│ ├── models.py # Database models<br>
│ ├── database.py # Database connection and session management<br>
│ <br>
├── data_structures # Data structures for in-memory processing<br>
│ ├── BinaryHeap.py - **TODO**<br>
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

<u>**To setup:**<br></u>
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Note: in pycharm use a venv interpreter

<u>**Install libs:**</u><br>
pip install flask yfinance plotly pandas sqlalchemy pandas_datareader setuptools yfinance[nospam]

<u>**to run:**</u><br>
python main.py 
after stats calculated go to to view Bubble chart:
http://127.0.0.1:5000/chart

<u>** Note: on initial run will take 5-10 min for database to build **</u><br>
Has a limit on API calls that shouldn't be spammed. 

