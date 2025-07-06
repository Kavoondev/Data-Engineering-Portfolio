# Weather Data Analytics ETL Pipeline

**A scalable ETL pipeline to collect, transform, and visualize weather data, showcasing data engineering skills for modern cloud-based analytics.**

## Overview
This project demonstrates a robust ETL pipeline that fetches weather data from two APIs (OpenWeatherMap and WeatherAPI), processes it using Apache Spark in Databricks, stores it in a Star Schema in MS SQL Server, orchestrates the workflow with Apache Airflow, and visualizes trends in Power BI. Built to showcase proficiency in **Data Integration**, **Database Development**, **Data Warehouse Development**, **Cloud Concepts**, and **Engineering Excellence**, this project is ideal for data engineering roles in the U.S. tech industry.

**Keywords**: Data Engineering, ETL Pipeline, Apache Airflow, Databricks, Spark, MS SQL Server, Power BI, Python, SQL, Delta Lake, Data Warehouse, Star Schema, Cloud Analytics.

![Airflow DAG](https://github.com/Kavoondev/Data-Engineering-Portfolio/blob/main/airflow_done.png?raw=true)

## Architecture
- **Extract**: Fetches JSON data from OpenWeatherMap (temperature, humidity) and WeatherAPI (precipitation) hourly, storing raw data in Databricks DBFS (`dbfs:/Volumes/workspace/default/weather/raw/`).
- **Transform**: Processes data in Databricks using PySpark, handling Spark part-files and NaN values, and saves as CSV in `dbfs:/Volumes/workspace/default/weather/transformed/`.
- **Load**: Populates a Star Schema in MS SQL Server (`weather_dwh` database) for analytical queries.
- **Orchestration**: Uses Apache Airflow 2.8.0 to schedule and manage the ETL workflow with an hourly DAG (`weather_etl`).
- **Visualization**: Power BI dashboard displays temperature and precipitation trends by city and date.

## Technologies
- **Python**: Pandas, Requests, pymssql for data extraction and loading.
- **SQL**: Star Schema design, analytical queries in MS SQL Server.
- **Apache Airflow 2.8.0**: Workflow orchestration with Databricks integration.
- **Databricks Community Edition**: Apache Spark, Delta Lake for data transformation.
- **MS SQL Server**: Data Warehouse with Star Schema.
- **Power BI**: Visualization of weather trends.
- **DBFS**: Storage for raw and transformed data (simulating cloud storage).

## Setup
### Prerequisites
- MS SQL Server (Express or Developer Edition) with two databases: `airflow_db` (Airflow metadata) and `weather_dwh` (Data Warehouse).
- Databricks Community Edition account.
- API keys for [OpenWeatherMap](https://openweathermap.org/) and [WeatherAPI](https://www.weatherapi.com/).
- Python 3.8+.

### Installation
1. Install dependencies:
   ```bash
   pip install apache-airflow==2.8.0 apache-airflow-providers-microsoft-mssql==3.9.2 apache-airflow-providers-databricks==6.7.0 pandas requests pymssql pytest databricks-cli python-dotenv connexion[swagger-ui]
   ```
2. Configure MS SQL Server:
   - Create databases: `airflow_db` and `weather_dwh`.
   - Enable `READ_COMMITTED_SNAPSHOT`:
     ```sql
     ALTER DATABASE airflow_db SET READ_COMMITTED_SNAPSHOT ON;
     ```
3. Configure Airflow:
   - Update `~/projects/airflow/pet/airflow.cfg`:
     ```
     sql_alchemy_conn = mssql+pymssql://sa:<your_password>@localhost:1433/airflow_db
     ```
   - Initialize database: `airflow db init`.
   - Create admin user: `airflow users create --username admin --password admin --firstname Admin --lastname Admin --role Admin --email kavoon.dev@gmail.com`.
   - Start Airflow: `airflow webserver -p 8080` and `airflow scheduler`.
4. Configure Databricks CLI and Airflow connection:
   - Set up `databricks_default` connection in Airflow UI (Admin > Connections).
5. Create `.env` file in the project root with:
   ```
   OPENWEATHER_API_KEY=your_openweather_key
   WEATHERAPI_API_KEY=your_weatherapi_key
   ```
6. Install Databricks CLI: `pip install databricks-cli`.

### Project Structure
- `extract_weather.py`: Fetches weather data from APIs and saves to DBFS.
- `transform_weather.py`: Processes data in Databricks, handles part-files and NaN values, saves as CSV.
- `load_to_mssql.py`: Loads transformed data into MS SQL Server Star Schema.
- `weather_dag.py`: Airflow DAG for hourly ETL orchestration.
- `tests/`: Unit tests using pytest for extract and transform steps.

## Usage
1. Run `extract_weather.py` to fetch and store raw data in DBFS.
2. Execute the Databricks Notebook (`/Users/your_username/transform_weather`) to transform data.
3. Run `load_to_mssql.py` to load data into `weather_dwh`.
4. Activate the `weather_etl` DAG in Airflow UI (`localhost:8080`).
5. Connect Power BI to MS SQL Server (`weather_dwh`) and build a dashboard with temperature and precipitation trends.

## Engineering Excellence
- **SOLID Principles**: Classes like `WeatherExtractor` and `WeatherTransformer` follow Single Responsibility.
- **DRY**: Reusable functions for data extraction and transformation.
- **KISS**: Simple SQL queries and modular Python code.
- **Unit Tests**: Pytest ensures reliability of extract and transform steps.
- **Data Quality**: Handles Spark part-files and NaN values for robust processing.
- **Documentation**: Clear setup and usage instructions for reproducibility.

## For Employers
This project showcases skills critical for data engineering roles:
- **Data Integration**: Seamlessly combines data from multiple APIs using Python and Airflow.
- **Database Development**: Implements a Star Schema in MS SQL Server for analytical queries.
- **Data Warehouse Development**: Leverages Delta Lake and Star Schema for scalable analytics.
- **Cloud Concepts**: Uses Databricks and DBFS, simulating Azure Blob Storage workflows.
- **Engineering Excellence**: Modular, tested, and well-documented code adhering to SOLID, DRY, and KISS principles.
- **Certifications**: Built with knowledge from the **Astronomer Airflow Fundamentals Certification**.

**Contact**: [kavoon.dev@gmail.com](mailto:kavoon.dev@gmail.com) | [Web-site](https://databylex.github.io/)

## License
MIT License