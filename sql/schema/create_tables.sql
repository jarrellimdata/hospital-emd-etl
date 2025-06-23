DROP TABLE IF EXISTS attendances;
CREATE TABLE attendances (
    date DATE,
    hospital TEXT,
    patient_count NUMERIC
);

DROP TABLE IF EXISTS wait_times;
CREATE TABLE wait_times (
    date DATE,
    hospital TEXT,
    wait_time NUMERIC
);

DROP TABLE IF EXISTS bed_occupancy;
CREATE TABLE bed_occupancy (
    date DATE,
    hospital TEXT,
    occupancy_rate NUMERIC
);

DROP TABLE IF EXISTS er_summary;
CREATE TABLE er_summary (
    date DATE,
    hospital TEXT,
    patient_count NUMERIC,
    wait_time NUMERIC,
    occupancy_rate NUMERIC
);