# Singapore Hospital A&E ETL Pipeline

---

## 📌 Project Overview
This project simulates a real-world data engineering pipeline using open hospital data from Singapore. It uses Python scripts to automate the ingestion, cleaning, transformation, and loading of healthcare data into a PostgreSQL database. The cleaned data is then explored in pgAdmin4 and visualized using Power BI.

---

## 🎯 Objective
To build a modular and reproducible data engineering workflow that prepares real-world hospital operations data for analysis, using tools such as Python, SQL, and Power BI.

---

## 🏥 Business Use Case
Support data-driven hospital operations by enabling consistent reporting on emergency department (ED) performance, capacity constraints, and service efficiency. The final dataset helps identify anomalies, bottlenecks, and system-wide pressure points for better healthcare planning and policy-making.


---

## 📂 Data Sources

Data was sourced from the Ministry of Health (MOH), Singapore:

- [Attendances at Emergency Medicine Departments](https://www.moh.gov.sg/others/resources-and-statistics/healthcare-institution-statistics-attendances-at-emergency-medicine-departments)
- [Waiting Time for Admission to Ward](https://www.moh.gov.sg/others/resources-and-statistics/healthcare-institution-statistics-waiting-time-for-admission-to-ward)
- [Bed Occupancy Rate (BOR)](https://www.moh.gov.sg/others/resources-and-statistics/healthcare-institution-statistics-beds-occupancy-rate-(bor))

Each dataset contains historical monthly records, updated as of July 2025. 

---

## 🧰 Tools and Technologies

- **Python**: pandas, sqlalchemy
- **PostgreSQL**: for storing processed data
- **pgAdmin4**: for database inspection and querying
- **Power BI**: for dashboarding
- **Jupyter Notebook / VS Code**: For development
- **Mermaid Live Editor**: For designing Entity Relationship Diagram (ERD)

---

## 🧱 Folder Structure

```
hospital-emd-etl/
├── data/
│   ├── raw/                      # Raw Excel files from MOH
│   └── processed/                # Cleaned and merged CSVs
├── logs/
│   └── etl_pipeline.log          # Pipeline logs
│   └── test_integration.log      # Integration test logs
├── scripts/
│   ├── new/
│   │   ├── extract_data_w_logging.py
│   │   ├── transform_data.py
│   │   └── load_to_postgres_w_logging.py
│   └── utils/
│       └── logger.py             # Custom logging setup
├── pipelines/
│   ├── pipeline_w_logging.py     # ETL orchestration script
│   └── run_pipeline.py           # Entry point
├── sql/
│   ├── create_tables.sql
│   ├── alter_tables.sql
│   └── analysis_queries.sql
├── dashboard/
│   ├── hospital_dashboard.pbix   # Power BI dashboard
│   └── screenshots/
├── diagrams/
│   └── erd.png                   # Entity Relationship Diagram
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_load.py
│   └── test_integration.py
├── config.yaml                   # Configs
├── .env                          # DB credentials (excluded from Git)
├── .gitignore                    # Ignored files
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
         
```

---

## ▶️ How to Run the Project

1. Ensure PostgreSQL is installed and running locally.
2. Update DB credentials in .env or directly in the script.
3. Download and place raw Excel files in data/raw/
4. Run the ETL pipeline:


```bash
python pipeline.py
```

---

## 🧮 PostgreSQL Tables
- attendances: Monthly patient counts
- wait_times: Median wait time to admission
- bed_occupancy: Bed occupancy rate
- er_summary: Combined view for analysis

---

## 🧾 SQL Utilities
- create_tables.sql: Defines and creates the base tables
- alter_tables.sql: Round/cast columns for easier analysis in PostgreSQL
- analysis_queries.sql: Sample queries to analyze trends

---

## 🗺️ Data Model
All tables are linked by date and hospital. The primary table for reporting is er_summary.

📎 Entity Relationship Diagram (ERD)
- Created using [Mermaid Live Editor](https://mermaid.live) and exported as an image:
![mermaid-ERD](https://github.com/user-attachments/assets/9fcb67e2-5e09-498c-bf84-70b6194d98d6)

---

## 📊 Power BI Dashboard
Includes visuals for:
- Monthly trends by hospital
- Median wait time
- Rolling 3-month averages
- Correlation analysis between variables

📎 Note: The dashboard is intentionally simple to highlight the data pipeline. It can be extended based on stakeholder needs.

**Snapshot:** 
![image](https://github.com/user-attachments/assets/19cfc0c5-fd45-480d-b0e3-0476aa234d11)

[Power BI Live Dashboard](https://app.powerbi.com/reportEmbed?reportId=531764bf-45e1-4dce-843d-5ac2d1f78af6&autoAuth=true&ctid=bd697c1b-c481-479c-841e-c618542675c3)

---

## 📈 Results / Findings
- Cleaned and merged >20,000 rows of hospital data
- Created a consistent structure for trend analysis
- Derived rolling averages and tracked key metrics
- Built SQL queries for exploratory reporting
- Implemented schema validation, logging, and both unit/integration testing for reliability

---

## 🚧 Limitations
- Manual data download (no API access)
- Local batch pipeline (no orchestration yet)
- Simplified dashboard due to limited context

---

## 🚀 Next Steps / Future Work
⚙️ Data Engineering & Deployment
- Containerize the pipeline using Docker
- Add Airflow orchestration for automated scheduling
- Explore cloud deployment (e.g. Azure, AWS)

📊 Analytics & Power BI
- Add anomaly detection and KPIs
- Enhance visual design in Power BI
- Document DAX measures

🧠 Stakeholder Collaboration
- Collaborate with healthcare domain experts for deeper insights

---

## 📚 References
- [Ministry of Health, Singapore](https://www.moh.gov.sg/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- [Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi)

---
## Acknowledgments:
Built as a personal portfolio project to demonstrate skills in data engineering, SQL, and healthcare analytics using public data.


