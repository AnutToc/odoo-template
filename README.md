# ODOO Templates

This is odoo templates
(Default Odoo17, PSQL15)
-----------------------------------

## Requirements:
Download and install Docker, Docker-Compose from https://www.docker.com/products/docker-desktop/

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