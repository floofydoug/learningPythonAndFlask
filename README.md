# learningPythonAndFlask
setting up my first flask server

## create database
psql; 
`CREATE DB homework_db`

### notes

Just wanted to give you a quick update. I flew back a couple hours ago from Seattle. I was a lot more involved in the family processions than I thought and I haven't gotten to spend as much time on this task as I would've liked. I"ll keep my word and still submit what I have by the end of day tomorrow, using whatever time I have left after my day job. However, it may not be complete. 

After 2 hours, I do have some takeaways, though. 

-I should use the built in sqlite3 for efficiency. Don't bother with PSQL. 
-I'll be using Python 2.7 because my xcode on this machine is not updated, and downloading that may take too long in order to start with python3. 
-Don't bother with psql. Python comes with sqlite3 module. 
-I'm creating a db with two tables: Transactions, and Invoices; One Invoice to Many Transactions (possibly)
-I've decided on a couple endpoints: 

1. POST /invoice/  (will create an invoice)
2. POST /transaction (will record a payment)
3. 