# silk_pipeline

Instructions:

from root directory of project:

```
open .env file and fill in 'API_KEY' value with api key for Silk api
mkdir output
docker-compose up --build
```

This will run an instance of MongoDB on localhost:27017. It will create a collection called "hosts" in database "db" containing the normalized
hosts pulled from the Qualys and Crowdstrike apis. The "_id" field of each document is the IP address of the corresponding host.

Running this app will also output a file called "visualization.png" to the output folder created under the root directory. This is an image
of a bar graph showing the distribution of operating systems by host. See file visualization.png in this repository for an example

Note:
This code uses pandas dataframes to process data - in a production environment at larger scale this would probably be changed to use something like Spark instead, perhaps running on an AWS EMR cluster
