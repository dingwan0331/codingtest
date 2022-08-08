/* 183. Customers Who Never Order */

/*
problem url : https://leetcode.com/problems/sales-person/
*/

SELECT name AS Customers FROM Customers WHERE id not in (SELECT customerId from Orders)