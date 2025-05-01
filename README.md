# Miniproject for Placement Eligibility Apps
**Objective**:
This Streamlit application connects to a MySQL database and fetches data based on user input.

## Requirements
* Python 3.x
* Streamlit
* PyMySQL
* Pandas

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
	* Eligibility Criteria: Fetches eligible students based on user input
	* Insights: Displays insights and statistics about the data

## Features
* Connects to a MySQL workbench database using environment variables
* Fetches eligible students based on user input
* Displays insights about the data


## Troubleshooting
* Make sure to install all dependencies and create a `.env` file with your MySQL database credentials
* Check the application logs for any errors



