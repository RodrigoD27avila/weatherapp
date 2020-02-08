Setup do backend

cd backend

python -m venv venv

pip install -r requirements.txt

venv/Scripts/activate.ps1 # no windows
source venv/bin/activate # no linux

$env:APP_DATABASE="db"
set APP_DATABASE="db"

$env:WEATHER_APP_ID="<appid do open weather>"
set APP_WEATHER_ID="<appid do open weather>"

uvicorn app:app

o servidor será iniciado em http://localhost:8000

para acessar a api do sweager acessar http://localhost:8000/docs

Setup do frontend

cd frontend

npm install
npm run build
npm install -g serve
serve -s build

o servidor de fontend será inicializado em http://localhost:5000
