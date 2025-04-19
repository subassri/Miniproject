# Miniproject for Placement Eligibility Apps
# MySQL Database Connection App

This Streamlit application connects to a MySQL database and fetches data based on user input.

## Requirements
* Python 3.x
* Streamlit
* PyMySQL
* Pandas
* Matplotlib
* Plotly
* dotenv

## Installation
1. Clone the repository: `git clone https://github.com/your-repo/mysql-app.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your MySQL database credentials:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=password
DB_NAME=database

4. Run the application: `streamlit run app.py`

## Usage
1. Navigate to the application URL: `http://localhost:8501`
2. Select a page from the navigation menu:
	* Home: Displays a welcome message
	* Eligibility Criteria: Fetches eligible students based on user input
	* Insights: Displays insights and statistics about the data
	* Visualization: Displays visualizations of the data
	* About: Displays information about the application

## Features
* Connects to a MySQL database using environment variables
* Fetches eligible students based on user input
* Displays insights and statistics about the data
* Visualizes data using Plotly
* Provides information about the application

## Troubleshooting
* Make sure to install all dependencies and create a `.env` file with your MySQL database credentials
* Check the application logs for any errors

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or pull request.


