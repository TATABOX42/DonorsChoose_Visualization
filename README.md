# DonorsChoose_Visualization
* Source Code for my blog post: [Interactive Data Visualization with D3.js, DC.js, Python, and MongoDB](http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/)

Author's blog : http://adilmoujahid.com

[Install MongoDB in Ubuntu 14.04](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/)


## Getting started

The dependencies for the project can be installed using

    $ pip install -r requirements.txt
    
<!--- VAGRANT IS NOT YET CONFIGURED. INSTALL LOCALLY INSTEAD
You can use ``Vagrant`` to start a machine with a MongoDB instance running
 
   $ vagrant up
-->

To initialize the database you need to download the data

    $ wget https://s3.amazonaws.com/open_data/csv/opendata_projects.zip && unzip opendata_projects.zip

and import it

    $ mongoimport -d donorschoose -c projects --type csv --file opendata_projects.csv --headerline

## Run the app

    $ python app.py
