# SELECT (CASE WHEN COUNT(PARENT))
# PARENT_ID,COUNT(*)
# FROM ECOLI_DATA
# GROUP BY PARENT_ID

SELECT P.ID, (CASE 
              WHEN C.PARENT_ID IS NULL THEN 0
              ELSE COUNT(*)
              END) AS CHILD_COUNT
FROM ECOLI_DATA P LEFT JOIN ECOLI_DATA C
ON P.ID = C.PARENT_ID
GROUP BY P.ID,C.PARENT_ID


