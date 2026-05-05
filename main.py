import pandas as pd
from datetime import datetime
import psutil
import socket
import sqlite3
import os
import time 

def log_progress(message):
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("code_log.txt","a") as f:
        f.write(timestamp+ ":" + message+'\n')

def extract_metrics():
    log_progress("Starting data extraction")
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    cpu_usage = round(psutil.cpu_percent(interval=None),2)
    memory_usage = round(psutil.virtual_memory().percent,2)
    host = socket.gethostname()
    metrics = {
        "timestamp" : timestamp,
        "cpu_percent": cpu_usage,
        "memory_percent":memory_usage,
        "host":host
    }
    log_progress("Data extraction completed")
    return metrics 

def transform_data(metrics):
    log_progress("Starting data transformation")

    df=pd.DataFrame([metrics])
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["cpu_percent"] = df["cpu_percent"].clip(lower=0, upper=100)
    df["memory_percent"] = df["memory_percent"].clip(lower=0, upper=100)
    df = df.dropna()
    log_progress("Data transformation completed")
    return df 

def load_to_csv(df):
    log_progress("Starting CSV loading")
    file_exists = os.path.isfile("System_metrics.csv")
    df.to_csv("System_metrics.csv",mode="a",index=False,header=not file_exists)
    log_progress("System metrics saved to CSV")

def load_to_sqlite(df):
    log_progress("Starting SQLite loading")
    database_name = "Metrics.db"
    conex = sqlite3.connect(database_name)
    df.to_sql("System_metrics",conex,if_exists="append",index = False)
    conex.close()
    log_progress("Data loaded to Database")

def run_pipeline():
    log_progress("ETL pipeline started")
    try:
        while True:
            metrics = extract_metrics()
            transformed_df = transform_data(metrics)
            load_to_csv(transformed_df)
            load_to_sqlite(transformed_df)

            log_progress("ETL cycle completed")
            time.sleep(20)
    except KeyboardInterrupt:
        log_progress("ETL pipeline stopped by user")

if __name__ == "__main__":
    run_pipeline()


