import xml.etree.ElementTree as ET
from webapp.models import Customer, Tenant
from flask_restful import Resource
from datetime import datetime
from webapp.app import db


class LoadDemoData(Resource):
    def post(self):
        tree = ET.parse('demo/demo_data.xml')
        root = tree.getroot()

        for record in root.findall('record'):
            model = record.get('model')
            fields = {field.get('name'): field.text for field in record.findall('field')}
            if model == 'tenant':
                tenant = Tenant(
                    name=fields['name'],
                    code=fields['code'],
                    is_verified=bool(fields['is_verified']),
                    is_enabled=bool(fields['is_enabled']),
                    verification_code=fields['verification_code']
                )
                db.session.add(tenant)
                db.session.flush()

            elif model == 'customer':
                customer = Customer(
                    name=fields['name'],
                    address=fields['address'],
                    phone=fields['phone'],
                    email=fields['email'],
                    tenant_id=tenant.id,
                    created_on=datetime.fromisoformat(fields['created_on']) if 'created_on' in fields else None,
                    created_by_id=int(fields['created_by_id']) if 'created_by_id' in fields else None,
                    is_enabled=bool(fields['is_enabled']),
                )
                db.session.add(customer)
        db.session.commit()
