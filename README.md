# ODOO Templates

This is an Odoo template for quick setup and deployment.  
(Default Odoo 17, PostgreSQL 15)

---

## **📌 Requirements**
Before using this template, install the following:

- **Docker & Docker Compose** → [Download](https://www.docker.com/products/docker-desktop)
- **pgAdmin 4** → [Download](https://www.pgadmin.org/download/)
- **Pre-commit Hooks** → `pip install pre-commit`

---

## **🚀 Getting Started**

### Build
```
docker-compose build
```

### Run
```
docker-compose up -d
```

### Stop
```
docker-compose down
```

### Restart
```
docker-compose restart
```

### Print logs (Exit with ctrl+c)
```
docker-compose logs -f --tail=20
```

### Print list containers
```
docker-compose ps -a
```

### Reset db
```
docker-compose down -v
```

### Create new volumn
```
docker volume create odoo(version)_postgres_data
```

### More Command
```
docker-compose --help
```

### Code Quality Check (OCA Code Check)
To ensure code quality and follow OCA standards, run the following checks

### Install Pre-commit Hooks
```
pip install pre-commit
pre-commit install
```

### Run Code Checks (Pre-commit)
```
pre-commit run --all-files
```

### Run Pylint for Odoo
```
pylint --load-plugins=pylint_odoo extra-addons/
```

### Run Black Formatting
```
black .
```

### Run Flake8 for Python Linting
```
flake8 extra-addons/
```

### Run Unit Tests (Pytest)
```
pytest
```

### Connect the Database (pgAdmin4)

open pgAdmin4 
right click on server > register > server

Connection TAB 

Hostname/address = localhost

PORT = 8069

Maintenance database = postgres

Usernam = odoo

Password = odoo 

### Error Handle

Error at the first time (AssertionError: /var/lib/odoo/sessions: directory is not writable) Use docker-compose down -v for reset DB then docker-compose up -d again