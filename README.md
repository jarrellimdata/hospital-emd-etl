# Singapore Hospital A&E ETL Pipeline

---

## 📌 Project Overview

This project simulates a real-world data engineering pipeline using open hospital data from Singapore. Using Python scripts, the workflow automates the ingestion, cleaning, transformation, and loading of healthcare data into a PostgreSQL database. The data is then explored in pgAdmin4 and prepared for downstream analytics, including dashboarding in Power BI.

---

## 🎯 Objective

To build a modular and reproducible data engineering workflow that prepares real-world hospital operations data for analysis, using industry-relevant tools such as Python, SQL, and Power BI.

---

## 🏥 Business Use Case

The goal is to support data-driven hospital operations by enabling consistent reporting on emergency department (ED) performance, capacity constraints, and service efficiency. This helps surface anomalies, bottlenecks, and system-wide pressure points over time, which are critical for healthcare planning, resource allocation, and policy-making.

---

## 📂 Data Sources

Data was sourced from the Ministry of Health (MOH), Singapore:

- [Attendances at Emergency Medicine Departments](https://www.moh.gov.sg/resources-statistics/singapore-health-facts/emergency-departments)
- [Waiting Time for Admission to Ward](https://www.moh.gov.sg/resources-statistics/performance-indicators/waiting-time-for-admission)
- [Bed Occupancy Rate (BOR)](https://www.moh.gov.sg/resources-statistics/singapore-health-facts/beds)

Each dataset contains historical monthly records, updated as of June 2025. 

---

## 🧰 Tools and Technologies

- **Python**: pandas, sqlalchemy
- **PostgreSQL**: for storing processed datasets
- **pgAdmin4**: for SQL queries and inspection
- **Power BI**: for dashboarding and visual storytelling
- **Jupyter Notebook / VS Code**: For development

---

## 🧱 Folder Structure

project-root/
│
├── data/
│ ├── raw/ # Raw Excel files from MOH
│ └── processed/ # Cleaned and merged CSVs
│
├── scripts/
│ ├── extract_data.py
│ ├── transform_data.py
│ └── load_to_postgres.py
│
├── sql/
│ ├── create_tables.sql
│ ├── alter_tables.sql
│ └── analysis_queries.sql
│
├── images/ # ERD or dashboard screenshots
│
├── pipeline.py # Main orchestrator script
└── README.md

---

## ▶️ How to Run the Project

1. Make sure PostgreSQL is installed and running locally.
2. Update the database credentials in `load_to_postgres.py` if needed.
3. Place the raw Excel files inside the `data/raw` folder.
4. Run the ETL pipeline:

```bash
python pipeline.py
```

---

## 🧮 PostgreSQL Tables
attendances: Monthly patient counts per hospital

wait_times: Median wait time to be admitted to ward

bed_occupancy: Monthly bed occupancy percentage

er_summary: Combined view of all three datasets

---

## 🧾 SQL Utilities
- create_tables.sql: Defines the base tables
- alter_tables.sql: Refines data types (e.g., round float → int or decimal)
- analysis_queries.sql: Sample queries to analyze trends and correlations

---

## 🗺️ Data Model
Four tables in PostgreSQL are linked by date and hospital. The main table for analysis is er_summary.

📎 Entity Relationship Diagram (ERD):
![mermaid-ERD](https://github.com/user-attachments/assets/9fcb67e2-5e09-498c-bf84-70b6194d98d6)

---

## 📈 Results / Findings
- Cleaned and merged >20,000 rows of hospital data
- Structured datasets for consistent monthly trend analysis
- Derived metrics like rolling 3-month averages, wait time trends, and correlation between occupancy and wait time
- Built SQL queries for downstream exploration and reporting

---

##📊 Power BI Dashboard
This project includes a Power BI dashboard visualizing:
- Monthly trends by hospital
- Efficiency metrics like average wait time
- Rolling 3-month averages
- Correlation analysis between variables

📎 Note: As the focus of this project is on data engineering, the Power BI dashboard included is intentionally simple. It can be further developed based on business questions, stakeholder needs, and integration of more domain-specific data.

---

🚧 Limitations
- Manual download of Excel files (no APIs available)
- No real-time processing or orchestration (designed for local batch runs)
- Dashboard and analysis rely on simplified metrics due to limited context

---

🚀 Next Steps / Future Work
- Add Airflow orchestration for automated scheduling
- Uontainerize pipeline with Docker
- Integrate anomaly detection or alerting
- Implement cloud migration (Azure or AWS) for scalability
- - Add unit tests and logging

---

📚 References
- [Ministry of Health, Singapore](https://www.moh.gov.sg/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/))
- [Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi)


