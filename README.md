# WeatherApp

## Setup do backend

Navegue até o diretório do projeto de Backend.

```
cd backend
```

Crie o virtual enviroment.

```
python -m venv venv
```

Ative o virtual enviroment.

```
venv/Scripts/activate.ps1 # no Windows
source venv/bin/activate # no Linux
```

Instale as dependências (recomendado utilizar o Python versão 3.8).

```
pip install -r requirements.txt
```

Adicione a variável de ambiente que define o nome do database, se a variável não for informada o database será persistino em memória.
```
$env:APP_DATABASE="db" # no Windows
set APP_DATABASE="db" # no Linux
```
Adicione a variável de ambiente que define a chave de api do open weather.

```
$env:WEATHER_APP_ID="<appid do open weather>" # no Windows
set APP_WEATHER_ID="<appid do open weather>" # no Linux
```

Para iniciar a aplicação basta rodar o comando abaixo:

```
uvicorn app:app
```

o servidor será iniciado em http://localhost:800 para acessar a página da documentação da API utilize a URL http://localhost:8000/docs.

## Setup do frontend

Navegue até a pasta do Frontend.

```
cd frontend
```

Instale as dependências do projeto.

```
npm install
```

Faça a geração da versão de produção.

```
npm run build
```

Instale o servidor de páginas estáticas.

```
npm install -g serve
```

Execute o servidor.

```
serve -s build
```

O servidor de frontend será inicializado em http://localhost:5000.


## Arquitetura da aplicação

A aplicação de backend consiste em uma API REST que utiliza a bibliotecas [FastAPI](https://fastapi.tiangolo.com/). Essa biblioteca permite a criação automática da documentação da API em [Swagger](https://swagger.io/). Já o banco de dados utilizado foi o [TinyDB](https://tinydb.readthedocs.io/en/latest/index.html). Esse banco de dados permite a persistência de objetos do python em formato JSON no disco ou em memória.

Já a aplicação de Frontend foi desenvolvida utilizando [React](https://reactjs.org/) com [React Router](https://reacttraining.com/react-router/web/guides/quick-start). O controle de estados da aplicação é feito utilizando React Hooks.

Foram criadas 3 endpoints na API:

```
GET /cities/
```

Retorna a lista de cidades e a previsão do tempo de cada uma.

```
POST /cities/
```

Adiciona uma cidade nova pelo seu nome. Antes de ser inserida a cidade é feito a consulta dos 5 dias de previsão do tempo. A inserção da previsão do tempo serve como cache.

```
GET /cities/<id da cidade>
```

Retona as informações de clima de uma cidade. Se a previsão do tempo passou de um dia o backend atualiza a previsão para essa cidade ao mesmo tempo que a consulta é realizada.

## Testes
Para realizar os testes basta adicionar a chave de API do open weather na variável de ambiente `WEATHER_APP_ID`.

```
$env:WEATHER_APP_ID="<appid do open weather>" # no Windows
set APP_WEATHER_ID="<appid do open weather>" # no Linux
```

E por fim executar o comando de testes da pasta backend.

```
pytest
```

