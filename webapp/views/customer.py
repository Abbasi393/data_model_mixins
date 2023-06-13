from flask_restful import Resource
from webapp.models import Customer
from webapp.app import db


class ListCustomer(Resource):
    def get(self):
        customers = db.session.query(Customer).all()
        customers = [customer.as_dict() for customer in customers]
        return customers
