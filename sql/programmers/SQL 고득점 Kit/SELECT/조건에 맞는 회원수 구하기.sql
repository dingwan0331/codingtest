-- 문제 URL = https://school.programmers.co.kr/learn/courses/30/lessons/131535

-- 코드를 입력하세요
SELECT Count(*) AS USERS 
FROM USER_INFO 
WHERE AGE BETWEEN 20 AND 29 AND YEAR(JOINED) = 2021