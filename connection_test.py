# Next import the Connection method from PyMongo by running the command below. This method will allow us to connect to MongoDB and query the data.

from pymongo import MongoClient

# Next, we will define 4 variables that represent respectively MongoDB IP address, MongoDB port, MongoDB database name and MongoDB collection name.

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'donorschoose'
COLLECTION_NAME = 'projects'

# Next, we will define the 5 attributes that we will use for our query. Note that we had to explicitly set the records unique id _id to False. If we don't do so, it will be included in the query's response.

FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}

# And finally, let's connect to MongoDB and retrieve all the records along the 5 attributes that we are interested in. We can do so by running the following.

connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
collection = connection[DBS_NAME][COLLECTION_NAME]
projects = collection.find(projection=FIELDS)

# All the records are stored in projects, we can print all them by running the following command.

for project in projects:
    print project
