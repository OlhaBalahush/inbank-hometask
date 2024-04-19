# inbank hometask

### Part 1: Aggregated Monthly Payments (SQL)

The query (query.sql): 

```
SELECT SUM(
        CASE
            WHEN C.CURRENCY_CODE = 'EUR' THEN P.AMOUNT
            ELSE P.AMOUNT * CR.EXCHANGE_RATE_TO_EUR
        END
    ) AS SUM_AMOUNT_EUR,
    P.TRANSACTION_DATE
FROM PAYMENTS P
    INNER JOIN CURRENCIES C ON P.CURRENCY = C.CURRENCY_ID
    LEFT JOIN CURRENCY_RATES CR ON P.CURRENCY = CR.CURRENCY_ID
    AND P.TRANSACTION_DATE = CR.EXCHANGE_DATE
    LEFT JOIN BLACKLIST B ON P.USER_ID_SENDER = B.USER_ID
WHERE C.END_DATE IS NULL
    AND B.USER_ID IS NULL
GROUP BY P.TRANSACTION_DATE;
```

What this query does:

- The `CASE` statement checks if the currency code is 'EUR', if it is, it uses the amount as is. Otherwise, it converts the amount using the exchange rate.
- The `INNER JOIN` with the `CURRENCIES` table ensures that only active currencies are included by checking if the `END_DATE` is `NULL`.
- The `LEFT JOIN` with the `BLACKLIST` table and the `B.USER_ID` is `NULL` condition in the `WHERE` clause ensure that payments from blacklisted users are excluded.
- It groups the results by the `TRANSACTION_DATE` and calculates the sum of the amounts in EUR.