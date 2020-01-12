## PoC

Launch all docker
- docker-compose -f docker-compose-RabbitMQ.yml up -d
- docker-compose -f docker-compose-nifi.yml up -d
- docker-compose -f docker-compose-Influx.yml up -d

Launch de deploy.py to deploy the exchange and queue on RarbbitMQ
- python deploy.py

Import the template PoC.xml on Nifi and change the passwords

Create the "stock" database on InfluxDB
- On Chronograf go to 	InfluxDB Admin -> Create Database 	and name it "stock"

Import Dashboard.json

Send some data with send.py, two argument are required :
- Drawer number (1,2,3)
- Data value (1 to 200)
example : python send.py 1 145


## Other files

- Drawer.xml : template to duplicate if you want other drawer.
- Ingest.xml : template to get the data from RabbitMQ, transform into InfluxDB data and send them to InfluxdB
- script_nifi : script use in the ingest template to transform the data to InfluxDB data

