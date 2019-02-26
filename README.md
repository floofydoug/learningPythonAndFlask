# learningPythonAndFlask
setting up my first flask server

# getting started
`flask run`. If database has not been initialized, try `flask init-db`


## create database
`psql; 
```CREATE DB homework_db```

### endpoints

1. POST /invoice/  (will create an invoice)
2. POST /transaction (will record a payment)
3. GET /invoice/{invoice_id} (will grab a report on the invoice)

