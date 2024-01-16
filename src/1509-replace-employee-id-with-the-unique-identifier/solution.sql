# Write your MySQL query statement below
SELECT unique_id, name
FROM Employees as Emp
LEFT JOIN EmployeeUNI as Uni
ON Uni.id = Emp.id
