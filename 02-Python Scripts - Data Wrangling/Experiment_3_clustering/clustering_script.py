
"""
The cluseting (experiment 3) - You will need to use bigML (auto ML platform)

Build the cluster and build a cosine vector for each for the documents/cluster 
And do the matching based on the abstract within that cluster of taking the most similar match. 

This model based on unigram (first run) - (one word relationships). Run the dataset based on bygram (second run) (two word relationships).

Use the training set to build the cluster model. And the 20 test sets you want to match to each of the document within the cluster 
And do the centroid analysis on the test sets. 

Two sources (one for test and one for training). With the training you create k means clusters , then you run the training data sets against that model.  
You set the centroid cluster on test and train sets. 



https://bigml.readthedocs.io/en/latest/101_cluster.html

https://bigml.readthedocs.io/en/latest/101_topic_model.html






R               | Pandas
-------------------------------
summary(df)     | df.describe()
head(df)        | df.head()
dim(df)         | df.shape
slice(df, 1:10) | df.iloc[:9]


 BIG ML api authorisation access
set BIGML_USERNAME=andymccall896
set BIGML_API_KEY=a84323db6918b0612ba61d50a127cc944b1a7357
set BIGML_AUTH=username^=%BIGML_USERNAME%;api_key^=%BIGML_API_KEY%

curl "https://bigml.io/andromeda/source?%BIGML_AUTH%"
"""
import pandas as pd
import scipy as scipy
import sklearn as sk
import os



api = BigML('andymccall896','a84323db6918b0612ba61d50a127cc944b1a7357')


source = api.create_source('C:/Users/andym/Desktop/Datafancy/Journal_managementNP/02-Python Scripts - Data Wrangling/Experiment_3_clustering/Datasets/BigML_Batchcentroid_60978ab6e4279b13af0066a1.csv')
dataset = api.create_dataset(source)
model = api.create_model(dataset)
prediction = api.create_prediction(model, \
    {"petal width": 1.75, "petal length": 2.45})
    
    
#####################################
#####################################
##### This is it (Not working) ######
    
#    from bigml.api import BigML
# step 0: creating a connection to the service (default credentials)
# check how to set your credentials in the Authentication section
api = BigML()
# step 1: creating a source from the data in your local "data/iris.csv" file
source = api.create_source("data/iris.csv")
# waiting for the source to be finished. Results will be stored in `source`
api.ok(source)
# step 3: creating a dataset from the previously created `source`
dataset = api.create_dataset(source)
# waiting for the dataset to be finished
api.ok(dataset)
# step 5: creating a cluster
cluster = api.create_cluster(dataset)
# waiting for the cluster to be finished
api.ok(cluster)
# the new input data to find the centroid. All numeric fields are to be
# provided.
input_data = {"petal length": 4, "sepal length": 2, "petal width": 3,
              "sepal width": 1, "species": "Iris-setosa"}
# getting the associated centroid
centroid = api.create_centroid(cluster, input_data)

######################################
######################################
###### This is not working ###########
#from bigml.domain import Domain
#from bigml.api import BigML

#domain_info = Domain(prediction_domain="my_prediction_server.bigml.com",
 #                    prediction_protocol="http")

cwd = os.getcwd()
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))
#### set the working directory
os.chdir('C:/Users/andym/Desktop/Datafancy/Journal_managementNP/04-final_datatsets')
os.listdir('C:/Users/andym/Desktop/Datafancy/Journal_managementNP/02-Python Scripts - Data Wrangling/Experiment_3_clustering/Datasets')

##############################################################################
##############################################################################
##### Will not be using the API to do the modeling building in Python or R

cosine_dataframe = pd.read_excel(r'C:/Users/andym/Desktop/Datafancy/Journal_managementNP/04-final_datatsets/cosine_journal_check_df_final_20.xlsx').dropna()
#### This dataframe is the unigram centroid
#### You need to recreate this output with the training set only 
dataframe_unigram = pd.read_csv(r'C:/Users/andym/Desktop/Datafancy/Journal_managementNP/02-Python Scripts - Data Wrangling/Experiment_3_clustering/Datasets/BigML_Batchcentroid_60978ab6e4279b13af0066a1.csv')

dataframe_unigram.shape
dataframe_unigram.head
dataframe_unigram.describe
dataframe_unigram.info

