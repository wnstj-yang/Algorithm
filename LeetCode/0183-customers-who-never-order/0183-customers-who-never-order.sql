# Write your MySQL query statement below
SELECT A.name AS Customers FROM CUSTOMERS AS A
LEFT JOIN ORDERS AS B ON A.id = B.customerId
WHERE B.customerId IS NULL