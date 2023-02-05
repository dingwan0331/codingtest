-- 문제 URL = https://school.programmers.co.kr/learn/courses/30/lessons/131120

-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH 
FROM MEMBER_PROFILE 
WHERE GENDER = "W" AND MONTH(DATE_OF_BIRTH)=3 AND TLNO IS NOT null