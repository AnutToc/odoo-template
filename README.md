# ODOO Templates

This is odoo templates
(Default Odoo17, PSQL15)
-----------------------------------

## Requirements:
Download and install Docker, Docker-Compose from 
https://www.docker.com/products/docker-desktop/            
Download and install pgAdmin4                                 
from https://www.pgadmin.org/download/
-----------------------------------
## Getting Starts

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

Error at the first time (AssertionError: /var/lib/odoo/sessions: directory is not writable)
Use docker-compose down -v for reset DB then docker-compose up -d again
