# fullstack-project

## Para iniciar o projeto, rode o commando abaixo
```sh
$ docker-compose up
```

## Para realizar as migrações, entre no container command-service
```sh
$ docker-compose run command-service bash
```

## Ou no query-service
```sh
$ docker-compose run query-service bash
```


## Dentro do container, rode o comando abaixo para criar a migração
```sh
$ python -m alembic revision -m "create products table"
```

## Depois o comando abaxio para atualizar o banco de dados
```sh
$ python -m alembic upgrade head
```