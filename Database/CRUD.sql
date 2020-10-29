-- Outputs a list of group representatives and their corresponding groups
SELECT Fname, Gid FROM student INNER JOIN ON Sid = Rep

-- Deleting some number of students with the given (Sid)s from the table STUDENT
DELETE FROM STUDENT
-- Deleting the student with Sid 3
WHERE Sid = 3;

-- Deleting some number of instructors with the given (Iid)s from the table INSTRUCTOR
DELETE FROM INSTRUCTOR
WHERE Iid = 2;
-- Return the deleted row from the table
RETURNING *;

-- Deleting some number of Student_Electives with the given (Sid)s from the table Student_Electives  
DELETE FROM Student_Electives
-- Deleting the Student_Elective courses with Sids 5 and 2
WHERE Sid IN (5, 2);

-- Updating a student's attribute with a new value
UPDATE STUDENT
-- Update the group's number
SET Group = 3
-- Given the student Sid 
WHERE Sid = 4 ; 

-- Updating a course's attribute with a new value
UPDATE COURSE
-- Update the course's number
SET Cname = 'new name'
-- Given the course Cid 
WHERE Cid = 1  ; 

-- Querying all the (Bdate)s from the table DEPENDENT
SELECT Bdate FROM DEPENDENT;

-- Querying all the (Email)s from the table STUDENT
SELECT Email FROM STUDENT
-- Given the group number
WHERE Group = 2 ;

-- Querying all the Courses that are taught by certain instructors (INNER JOIN)
SELECT
    INSTRUCTOR.Iid,
    iname,
    COURSE.Cname
FROM
    INSTRUCTOR
INNER JOIN COURSE
-- Comparing by the instructor's Iid
    ON INSTRUCTOR.Iid = COURSE.Cid;

-- Querying all the Students with the same Group (LEFT JOIN)
SELECT
    Sid,
    Email,
    Year
FROM
    STUDENT
LEFT JOIN GRP
   -- Comparing by the GRP representatives
   ON STUDENT.Sid = Rep;


-- Querying all the courses and the student electives (FULL OUTER JOIN) 
SELECT
    COURSE.Cid,
    Cname
FROM
    Student_Electives
    FULL OUTER JOIN COURSE
    -- Comparing by COURSE and Student_Electives Cid
    ON COURSE.CID = Student_Electives.Cid
