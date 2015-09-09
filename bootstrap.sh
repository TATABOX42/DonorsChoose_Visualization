#!/usr/bin/env bash

# install python-pip
sudo apt-get install -y python-pip 
# update repositories
apt-get update && 
# install mongo
sudo apt-get install -y mongodb
# install pip requirements
sudo pip install -r requirements.txt
# download database
wget https://s3.amazonaws.com/open_data/csv/opendata_projects.zip && unzip opendata_projects.zip
# mongo install database
mongoimport -d donorschoose -c projects --type csv --file opendata_projects.csv --headerline

mongo
# in mongo terminal do
use donorschoose
show collections
db.projects.findOne()
db.projects.findOne({}, {school_state:1, resource_type:1, poverty_level:1, date_posted:1, total_donations:1, funding_status:1, _id:0})

db.projects.find({}, {school_state:1, resource_type:1, poverty_level:1, date_posted:1, total_donations:1, funding_status:1, _id:0})