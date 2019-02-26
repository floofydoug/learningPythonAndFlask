# learningPythonAndFlask
setting up my first flask server

# getting started
`flask run`. If database has not been initialized, try `flask init-db`


## create database
psql; 
`CREATE DB homework_db`

### notes

After 2 hours, I do have some takeaways, though. 

-I should use the built in sqlite3 for efficiency. Don't bother with PSQL. 
-I'll be using Python 2.7 because my xcode on this machine is not updated, and downloading that may take too long in order to start with python3. 
-Don't bother with psql. Python comes with sqlite3 module. 
-I'm creating a db with two tables: Transactions, and Invoices; One Invoice to Many Transactions (possibly)
-I've decided on a couple endpoints: 

1. POST /invoice/  (will create an invoice)
2. POST /transaction (will record a payment)
3. GET /invoice/{invoice_id} (will grab a report on the invoice)

