/* leetcode 182.duplicate emails */

/* 
problem url : https://leetcode.com/problems/duplicate-emails/
*/

SELECT email from Person GROUP BY email HAVING COUNT(email) > 1