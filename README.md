## Install all requirements
```
pip install -r requirements.txt
```

## Create database
```
CREATE DATABASE database_name;
```

## Run server
```
python bin/manager.py runserver
```
## Run database migration
```
python bin/manager.py db stamp head
python bin/manager.py db migrate
python bin/manager.py db upgrade
```
## Run redis worker
```
python bin/redis_worker.py
```