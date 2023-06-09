import xml.etree.ElementTree as ET
from datetime import datetime
from webapp import db, with_app_context
from webapp.models import Customer


@with_app_context
def insert_demo_data():
    tree = ET.parse('demo_data.xml')
    root = tree.getroot()

    for record in root.findall('record'):
        model = record.get('model')
        fields = {field.get('name'): field.text for field in record.findall('field')}

        if model == 'customer':
            customer = Customer(
                name=fields['name'],
                address=fields['address'],
                phone=fields['phone'],
                email=fields['email'],
                is_enabled=bool(fields['is_enabled']),
                created_on=datetime.fromisoformat(fields['created_on']),
                created_by_id=int(fields['created_by_id'])
            )

            # Set optional fields if provided
            if 'modified_on' in fields:
                customer.modified_on = datetime.fromisoformat(fields['modified_on'])
            if 'modified_by_id' in fields:
                customer.modified_by_id = int(fields['modified_by_id'])
            db.session.add(customer)
    db.session.commit()


insert_demo_data()