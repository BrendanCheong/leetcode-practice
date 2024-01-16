# Write your MySQL query statement below
SELECT name, population, area FROM World
WHERE area >= 3 * POW(10, 6)
OR population >= 25 * POW(10, 6);
