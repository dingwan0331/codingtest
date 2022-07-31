/* leetcode 607.Sales Person */

/*
problem url : https://leetcode.com/problems/sales-person/
*/

/* 1번 방법 Sub Query*/
SELECT name FROM SalesPerson WHERE sales_id not in (
    SELECT sales_id from Orders WHERE com_id in (
        SELECT com_id from Company WHERE name = "RED"
    ) 
)
/* 결과 
Runtime: 1970 ms, faster than 31.68% of MySQL online submissions for Sales Person.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Sales Person.
*/

/* 2번 방법 JOIN */

SELECT
    s.name
FROM
    salesperson s
WHERE
    s.sales_id NOT IN (SELECT
            o.sales_id
        FROM
            orders o
                LEFT JOIN
            company c ON o.com_id = c.com_id
        WHERE
            c.name = 'RED')
;