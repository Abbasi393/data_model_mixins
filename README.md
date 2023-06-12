# Data Model Mixins
This project showcases an example implementation of model mixins using SQLAlchemy, a popular Object-Relational Mapping (ORM) library for Python. The project demonstrates how model mixins can enhance code reusability and modularity in SQLAlchemy-based applications.


## Environment setup

Create a virtual env:
```
python3 -m venv venv
source venv/bin/activate
```

Install packages from requirements.txt:
```
pip install -r requirements.txt
```

## Run app
You need to set the following environment variables
```
export DB_NAME=db_name
export DB_HOST=db_host
export DB_PASSWORD=db_password
export DB_USER=db_user
```

Run app with:
```
flask db upgrade
flask run
```

### Upgrade and Migrate DB (Optional)

If we modify DB Schema or add/change fields datatype or name, we should upgrade the database Schema. So for this you may export environment variables
```
export DB_NAME=db_name
export DB_HOST=db_host
export DB_PASSWORD=db_password
export DB_USER=db_user
```

and then upgrade the DB Schema

```
(venv)> flask db upgrade
```