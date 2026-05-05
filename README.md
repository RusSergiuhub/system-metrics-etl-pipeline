# System Data Processing Pipeline

A basic ETL pipeline that collects local system metrics such as CPU usage, memory usage and hostname, transforms the data using Pandas, and stores the results in CSV and SQLite format.

## Features
- Collects CPU and memory usage using psutil
- Adds timestamp and host information
- Cleans and transforms data using Pandas
- Stores processed data in CSV format
- Stores processed data in SQLite database
- Logs ETL progress to a log file

## Tech Stack
- Python
- Pandas
- psutil
- SQLite
