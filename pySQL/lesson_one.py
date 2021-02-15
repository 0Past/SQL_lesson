from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, DateTime, Boolean, ForeignKey, create_engine)

engine = create_engine('sqlite:///listings.db')

metadata = MetaData()

employees = Table('employees', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('name', String(32), nullable=False),
                  Column('surname', String(32), nullable=False),
                  Column('birthday', DateTime(), nullable=False),
                  Column('post', String(32), nullable=False),
                  extend_existing=True
                  )

client_info = Table('client_info', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('postcode', Integer(), nullable=False),
                    Column('city', String(32), nullable=False),
                    Column('street', String(32), nullable=False),
                    Column('apartments', Integer(), nullable=False),
                    Column('birthday', DateTime(), nullable=False),
                    Column('phone', String(32), nullable=False),
                    Column('email', String(32), nullable=False),
                    extend_existing=True
                    )

clients = Table('clients', metadata,
                Column('id', Integer(), primary_key=True),
                Column('name', String(32), nullable=False),
                Column('surname', String(32), nullable=False),
                Column('client_info_id', Integer(), ForeignKey('client_info.id')),
                extend_existing=True
                )

bills = Table('bills', metadata,
              Column('number', Integer(), primary_key=True),
              Column('date', DateTime(), nullable=False),
              Column('client_id', Integer(), ForeignKey('clients.id')),
              Column('employee_id', Integer(), ForeignKey('employees.id')),
              extend_existing=True
              )

passwords = Table('passwords', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('login', String(32), nullable=False),
                  Column('password', String(32), nullable=False),
                  Column('account', Integer(), nullable=False),
                  Column('client_id', Integer(), ForeignKey('clients.id')),
                  extend_existing=True
                  )

client_account = Table('client_accounts', metadata,
                       Column('id', Integer(), primary_key=True),
                       Column('amount', Integer(), nullable=False),
                       Column('bill', Integer(), nullable=False),
                       Column('bill_number', Integer(), ForeignKey('bills.number')),
                       extend_existing=True
                       )

operations = Table('operations', metadata,
                   Column('id', Integer(), primary_key=True),
                   Column('amount', Integer(), nullable=False),
                   Column('date', DateTime(), nullable=False),
                   Column('client_account_id', Integer(), ForeignKey('client_accounts.id')),
                   extend_existing=True
                   )

metadata.create_all(engine)
