# FlaskArchitecture
Define main structure for flask server with models, presistence, managers and routes layers.  
Also define configs for server like Development, Staging, Production and Test.  
Contain ORM database with migrations, redis worker with redis server and example for env and blueprints to register routes.  

## Install requirements
```
pip install -r requirements.txt
```

## Database (alembic/migrations)
#### Create database
```
CREATE DATABASE database_name;
```

#### Run database migration
```
python bin/manager.py db stamp head
python bin/manager.py db migrate
python bin/manager.py db upgrade
```

#### Add migration with specific id 
```
python bin/manager.py db revision --rev-id REV_ID
```

#### Init alembic migration
```
python bin/manager.py db init
```

#### Print help for alembic migration 
```
python bin/manager.py db -?
```

## Run server
```
python bin/manager.py runserver
```

## Run redis worker
```
python bin/manager.py redis-worker
```

## Run redis server
```
python bin/manager.py redis-server
```

---
All commands can be terminated by CTRL+C, some need after that ENTER
