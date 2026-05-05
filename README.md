# System Data Processing Pipeline

A Python-based ETL pipeline that collects local system metrics (CPU and memory usage), processes the data using Pandas, and stores structured results in CSV and SQLite for monitoring and future analysis.

---

## Features

- Collects real-time CPU and memory usage using psutil  
- Adds timestamp and host information to each record  
- Performs data cleaning and transformation using Pandas  
- Stores processed data in CSV format  
- Stores structured data in a SQLite database  
- Logs ETL execution steps in a text file  

---

## Technologies Used

- Python  
- Pandas  
- psutil  
- SQLite  
- CSV  
- Logging  

---

## Project Structure
│
├── main.py
├── system_metrics.csv
├── Metrics.db
├── code_log.txt

---

## Future Improvements

- Implement anomaly detection using Isolation Forest  
- Perform time-series feature engineering (windowing, statistics)  
- Add real-time anomaly detection capabilities  
- Implement alerting system (email notifications)  
- Expose functionality via FastAPI microservice  
- Containerize the application using Docker  
