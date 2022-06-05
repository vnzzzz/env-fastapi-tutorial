# env-fastapi

- fastapiの開発環境をつくる


.venv/bin/gunicorn -w 1 -k uvicorn.workers.UvicornWorker --capture-output --log-level warning --access-logfile - --bind :80 app.main:app
