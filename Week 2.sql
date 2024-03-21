-- create students table
CREATE TABLE students (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(50),
    age INTEGER,
    campus_id INTEGER,
    total_grade FLOAT
);

-- create campus table
CREATE TABLE campus (
    id SERIAL PRIMARY KEY,
    campus_name VARCHAR(50),
    batch VARCHAR(10),
    start_date DATE
);

-- Insert data into the students table
INSERT INTO students (name, age, campus_id, total_grade)
VALUES
    ('Rafif Iman', 20, 1, 85.5),
    ('Hana Arisona', 21, 2, 90.2),
    ('Raka Purnomo', 19, 1, 78.9),
    ('Danu Irfansyah', 20, 3, 92.7),
    ('Rachman Ardhi', 22, 2, 88.1);

-- Insert data into the campus table
INSERT INTO campus (campus_name, batch, start_date)
VALUES
    ('Remote', 'RMT-1', '2023-01-01'),
    ('Jakarta', 'HCK-2', '2023-02-01'),
    ('BSD', 'BSD-4', '2023-03-01'),
    ('Surabaya', 'SUB-1', '2023-04-01'),
    ('Singapore', 'SIN-1', '2023-05-01');

--ganti kak hana jadi 95.3
UPDATE Students 
SET total_grade = 95.3
WHERE id = 2 ;

UPDATE Students 
SET total_grade = 95.3
WHERE id = 1 ;

DELETE FROM Students
WHERE id = 6;

DELETE FROM campus
WHERE id = 5;

INSERT INTO students (name, age, campus_id, total_grade)
VALUES
	('Adhy Arya Hendrata', 17, 1, 89.9);

--EXPLAIN 
SELECT students.name, students.age, campus.campus_name
FROM students
JOIN campus 
ON Students.campus_id = campus.id
WHERE campus.campus_name = 'Jakarta';

--coba coba 
EXPLAIN
SELECT st.name, st.age, camp.campus_name
FROM students as st
JOIN campus as camp
ON st.campus_id = camp.id
WHERE camp.campus_name = 'BSD';

TRUNCATE TABLE Students;

DROP TABLE Students;



select * from students
select * from campus

