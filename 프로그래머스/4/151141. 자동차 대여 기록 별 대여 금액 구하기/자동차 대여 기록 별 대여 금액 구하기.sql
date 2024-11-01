WITH A AS (
    SELECT
        C.DAILY_FEE,
        H.HISTORY_ID,
        CASE WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1 < 7 THEN 0
            WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1 >= 90 THEN (SELECT DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                                               WHERE DURATION_TYPE = '90일 이상'
                                                                AND CAR_TYPE = '트럭') / 100 
            WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1 >= 30 THEN (SELECT DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                                               WHERE DURATION_TYPE = '30일 이상'
                                                                AND CAR_TYPE = '트럭') / 100
            WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1 >= 7 THEN (SELECT DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                                               WHERE DURATION_TYPE = '7일 이상'
                                                               AND CAR_TYPE = '트럭') / 100       
        END AS DISCOUNT_RATE,
        DATEDIFF(H.END_DATE,H.START_DATE)+1 AS DATE_DIFF
        # CASE WHEN P.DURATION_TYPE = '7일 이상' THEN 7
        #     WHEN P.DURATION_TYPE = '30일 이상' THEN 30
        #     WHEN P.DURATION_TYPE = '90일 이상' THEN 90
        # END AS DURATION
    FROM CAR_RENTAL_COMPANY_CAR C JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
    ON C.CAR_ID = H.CAR_ID
    # JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
    # ON C.CAR_TYPE = P.CAR_TYPE    
    WHERE C.CAR_TYPE = '트럭'
)

# SELECT *
# FROM A
SELECT
    HISTORY_ID,
    ROUND(DAILY_FEE * DATE_DIFF * (1-DISCOUNT_RATE)) AS FEE
FROM A
ORDER BY FEE DESC, HISTORY_ID DESC
    
    

    
