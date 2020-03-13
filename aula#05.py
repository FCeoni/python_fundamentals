#=============================================================================================
#       aula#05 - 13/03/2020  - Python com Post
#=============================================================================================

# instalar pacotes
# 1 - sudo apt install postgresql
# 2 - sudo apt install mongodb
# 3 -  mongo 
# prompt=>  > 
# sair =>  ctrl + c 
#
#
# 4 - sudo apt install virtualenv 
# 5 - virtualenv -p python3 venv
# prompt=>  (venv) developer@Developer:~/python_fundamentals$ 
# 6 - pip install psycopg2-binary  - instalar qdo houver quebra de permissão
# 7 - create user admin password '4linux';
# 8 - create database projeto owner admin;

# 

#=============================================================================================
#       aula#05 - 13/03/2020  - Python com SQLAlchemy - Abstração de DB como Framework
#=============================================================================================


# . /venv/bin/activate          # ativa a virtualenv

# pip install sqlalchemy

# sudo apt install sqlite3

# sudo apt update

# sudo apt install libsqlite3-dev

# sudo apt install sqlitebrowser

# criar pasta /app/core/core.py

 # -*- coding: utf-8 -*-

from sqlalchemy import (create_engine, MetaData, Column,
                            Table, Integer,
                            String, DateTime)

from datetime import datetime

engine = create_engine('sqlite:///banco.db', echo=True)
metadata = MetaData(bind=engine
user_table = Table('usuarios', 
                    metadata,
                        Colum('id', Integer, primary_key=True),
                        Colum('nome', String(40), index=True),
                        Colum('idade', Integer, nullabble=True),
                        Colum('senha', String),
                        Colum('criado em', DateTime, default=datetime.now),
                        Colum('atualizado em', DateTime, onupdate=datetime.now)
                        )

metadata.create_all(engine)