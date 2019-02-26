import os
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from db import get_db
from datetime import datetime, timedelta

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'homework.sqlite'),
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # endpoint expects data object to contain
    # amount, invoice_id, 
    @app.route('/transaction', methods=["POST"])
    def postTransaction():
        print(request.data)
        req_data = request.get_json()
        db = get_db()
        db.execute(
                'INSERT INTO transactions (amount, invoice_id) VALUES (?, ?)',
                (req_data["amount"], req_data["invoice_id"])
            )
        db.commit()
        return "successfully created a transaction"
    
    @app.route('/invoice', methods=["POST"])
    def createInvoice():
        req_data = request.get_json()
        db = get_db()
        db.execute(
            'INSERT INTO invoices (amount, due_date, description) VALUES (?, ?, ?)', 
            (req_data['amount'], req_data['due_date'], req_data['description'])  
        )
        db.commit()
        return "successfully created an invoice"

    @app.route('/invoice/<invoice_id>', methods=["GET"])  
    def getInvoice(invoice_id): 
        db = get_db()
        row = db.execute('SELECT * FROM invoices where invoice_id = ?', (invoice_id)).fetchone()
        total_paid = db.execute('SELECT SUM(amount) as total from transactions where invoice_id = ? ', (invoice_id)).fetchone()

        def calculateDaysPastDue(date):
            if date > datetime.now(): 
                print(date, date.now())
                return "current"
            else:
                print(date, date.now())
                delta = datetime.now() - date
                return delta.days + " days overdue" 

        return jsonify(description=row['description'], 
                       due_date=row['due_date'], 
                       original_amount=row['amount'], 
                       status=calculateDaysPastDue(row['due_date']),
                       total_paid=total_paid['total'])
            

    from . import db
    db.init_app(app)

    return app