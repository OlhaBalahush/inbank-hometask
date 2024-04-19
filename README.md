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

### Part 2: Weekend Data Processing (Python)

The code for the second part of the task is located in `data_processing.py`, and the result of running the script is saved in `combined_data.csv`.

This script reads the two CSV files, combines them, and adds a new column with the file generation date. The new combined CSV is then saved to `combined_data.csv`.

To run the code, follow these steps:

```
pip install pandas

python3 data_processing.py
```
