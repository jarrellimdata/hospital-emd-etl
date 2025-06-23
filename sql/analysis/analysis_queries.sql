-- 1. Average wait time by hospital
SELECT 
    hospital, 
    ROUND(AVG(wait_time), 2) AS avg_wait_time 
FROM er_summary
GROUP BY hospital
ORDER BY avg_wait_time DESC;

-- 2. Monthly trends for SGH
SELECT 
    TO_CHAR(date, 'YYYY-MM') AS year_month,
    ROUND(AVG(patient_count), 2) AS avg_patient_count,
    ROUND(AVG(wait_time), 2) AS avg_wait_time,
    ROUND(AVG(occupancy_rate), 2) AS avg_occupancy_rate
FROM er_summary
WHERE hospital = 'SGH'
GROUP BY year_month
ORDER BY year_month;

-- 3. Monthly patient volume per hospital
SELECT 
    TO_CHAR(date, 'YYYY-MM') AS year_month,
    hospital,
    SUM(patient_count) AS total_patients
FROM er_summary
GROUP BY hospital, year_month
ORDER BY hospital, year_month;

-- 4. Rolling 3-month average
WITH monthly_totals AS (
    SELECT 
        hospital,
        DATE_TRUNC('month', date) AS month_start,
        SUM(patient_count) AS total_patients
    FROM er_summary
    GROUP BY hospital, month_start
)
SELECT 
    hospital,
    TO_CHAR(month_start, 'YYYY-MM') AS year_month,
    total_patients,
    ROUND(
        AVG(total_patients) OVER (
            PARTITION BY hospital 
            ORDER BY month_start 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ), 2
    ) AS rolling_3month_avg
FROM monthly_totals
ORDER BY hospital, month_start;

-- 5. Correlation between occupancy and wait time
SELECT 
    hospital,
    ROUND(CORR(occupancy_rate, wait_time)::numeric, 2) AS correlation
FROM er_summary
GROUP BY hospital
ORDER BY correlation DESC;

-- 6. Materialized join of all tables
CREATE TABLE er_metrics_summary AS
SELECT 
    a.date,
    a.hospital,
    a.patient_count,
    w.wait_time,
    b.occupancy_rate
FROM attendances a
LEFT JOIN wait_times w
    ON a.date = w.date AND a.hospital = w.hospital
LEFT JOIN bed_occupancy b
    ON a.date = b.date AND a.hospital = b.hospital;

SELECT * FROM er_metrics_summary ; 












