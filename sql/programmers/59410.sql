/* NULL 처리하기 */

/*
problem url : https://school.programmers.co.kr/learn/courses/30/lessons/59410
*/

-- IFNULL 사용
-- SELECT ANIMAL_TYPE, IFNULL(NAME,'No name'), SEX_UPON_INTAKE FROM ANIMAL_INS

SELECT ANIMAL_TYPE, CASE WHEN NAME IS NULL THEN 'No name' ELSE NAME END, SEX_UPON_INTAKE FROM ANIMAL_INS