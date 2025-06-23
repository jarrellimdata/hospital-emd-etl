-- Round and cast columns to appropriate types

-- Attendances
ALTER TABLE attendances
ALTER COLUMN patient_count TYPE INTEGER
USING ROUND(patient_count);

-- Wait Times
ALTER TABLE wait_times
ALTER COLUMN wait_time TYPE NUMERIC(5,2)
USING ROUND(wait_time::numeric, 2);

-- Bed Occupancy
ALTER TABLE bed_occupancy
ALTER COLUMN occupancy_rate TYPE NUMERIC(6,3)
USING ROUND(occupancy_rate::numeric, 3);

-- ER Summary
ALTER TABLE er_summary
ALTER COLUMN patient_count TYPE INTEGER
USING ROUND(patient_count);

ALTER TABLE er_summary
ALTER COLUMN wait_time TYPE NUMERIC(5,2)
USING ROUND(wait_time::numeric, 2);

ALTER TABLE er_summary
ALTER COLUMN occupancy_rate TYPE NUMERIC(5,3)
USING ROUND(occupancy_rate::numeric, 3);
