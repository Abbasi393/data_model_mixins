from flask import Blueprint
from flask_restful import Api
from .seeds import LoadDemoData
from .customer import ListCustomer
seed_bp = Blueprint('seed_bp', __name__)
customer_bp = Blueprint('customer_bp', __name__)

seed_api = Api(seed_bp)
seed_api.add_resource(LoadDemoData, '/load_demo_data')

customer_api = Api(customer_bp)
customer_api.add_resource(ListCustomer, '/customer')
