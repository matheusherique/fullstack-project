# Fullstack Project

## Instalação e Configuração

### Para iniciar o projeto, rode o commando abaixo
```sh
$ docker-compose up
```

### Para realizar as migrações, entre no container command-service
```sh
$ docker-compose run command-service bash
```

### Ou no query-service
```sh
$ docker-compose run query-service bash
```


### Dentro do container, rode o comando abaixo para criar a migração
```sh
$ python -m alembic revision -m "create products table"
```

### Depois o comando abaixo para atualizar o banco de dados
```sh
$ python -m alembic upgrade head
```

## Documentação
Para acessar a documentação da API, basta acessar os seguintes links (após iniciar o projeto)

### Query API
[ReDoc](http://localhost:8002/redoc) ou [Swagger](http://localhost:8002/docs)

### Command API
[ReDoc](http://localhost:8001/redoc) ou [Swagger](http://localhost:8001/docs)

## Endpoints
### Command Service
- POST /api/v1/products/ - Cria um novo produto.
- PUT /api/v1/products/{product_id} - Atualiza um produto existente.
- DELETE /api/v1/products/{product_id} - Exclui um produto existente.

### Query Service
- GET /api/v1/products/{product_id} - Retorna os detalhes de um produto.
- GET /api/v1/products/ - Lista todos os produtos.