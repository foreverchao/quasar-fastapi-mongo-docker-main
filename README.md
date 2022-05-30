# quasar-fastapi-mongo-docker

### Start the project in development mode

```bash
docker-compose up -d --build
```

### Into the MongoDB Bash in development mode

#### Get mongo CONTAINER ID
```bash
docker ps
```

#### Into mongo bash
```bash
docker exec -it <CONTAINER ID> bash

mongo

```

### Develope update

```
docker-compose build --pull
docker-compose up -d
```

### Run Local 

frontend:
127.0.0.1:3000

backend:
127.0.0.1:5000

backend docs(Swagger docs):
127.0.0.1:5000/docs