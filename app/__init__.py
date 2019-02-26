import os
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from db import get_db

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
        db = get_db()
        db.execute(
                'INSERT INTO transactions (amount, invoice_id) VALUES (?, ?)',
                (request.data.amount, request.data.invoice_id)
            )
        db.commit()
        return "Successfully Saved"
    
    @app.route('/invoice', methods=["POST"])
    def createInvoice():
        req_data = request.get_json()
        db = get_db()
        db.execute(
            'INSERT INTO invoices (amount, due_date, description) VALUES (?, ?, ?)', 
            (req_data['amount'], req_data['due_date'], req_data['description'])  
        )
        db.commit()
        return "Saved Invoice"

    @app.route('/invoice/<invoice_id>', methods=["GET"])  
    def getInvoice(invoice_id): 
        db = get_db()
        invoice = db.execute('SELECT * FROM invoices where invoice_id = ?', (invoice_id)).fetchone()
        print(invoice)
        return "got something"


    from . import db
    db.init_app(app)

    return app