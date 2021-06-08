
"""
Created on Sun May 23 13:03:34 2021
@author: andym
Cluserting modeling experiment 3
"""

#### Import packages 
import pandas as pd
import scipy as scipy
import sklearn as sk
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests ### this package allows me to run the script with a single line of code 


###### vectorising IDF function scripts
exec(open('C:/Users/andym/Desktop/Datafancy/Journal_managementNP/02-Python Scripts - Data Wrangling/Experiment_3_clustering/word_count_df_function.py').read())

####
#### the selected 20 cases will be used for evaluating the 
####

cosine_dataframe = pd.read_excel(r'C:/Users/andym/Desktop/Datafancy/Journal_managementNP/04-final_datatsets/cosine_journal_check_df_final_20.xlsx').dropna()
os.listdir('C:/Users/andym/Desktop/Datafancy/Journal_managementNP/02-Python Scripts - Data Wrangling/Experiment_3_clustering/Datasets/model data')

cosine_dataframe.columns
cosine_dataframe["Lens ID_Test "]
cosine_dataframe.shape
cosine_dataframe.head
cosine_dataframe.describe
cosine_dataframe.info
cosine_dataframe.shape

#### This dataframe is the unigram centroid
#### You need to recreate this output with the training set only 
#### You will need to figrue out how to 

#### test with k8 clusters unigram dataset
#### build the model on the train set and use the batch centroid to classify onto the test set 
#### will need to use a windows anlaytics function to slelect the highest score for cosine similarity 
eval_test_list= cosine_dataframe["Lens ID_Test "]

test_centroids_k8 = pd.read_csv("C:/Users/andym/Desktop/Datafancy/Journal_managementNP/02-Python Scripts - Data Wrangling/Experiment_3_clustering/Datasets/model data/2921-05-23-K-6-Testing-Centroid.csv")
train_centroids_k8 = pd.read_csv("C:/Users/andym/Desktop/Datafancy/Journal_managementNP/02-Python Scripts - Data Wrangling/Experiment_3_clustering/Datasets/model data/2921-05-23-K-6-Training-Centroid.csv")

test_centroids_k8['case_type'] = 'test'
train_centroids_k8['case_type'] = 'train'
 
test_centroids_k8_20 = test_centroids_k8[test_centroids_k8['Lens ID'].isin(cosine_dataframe["Lens ID_Test "])]
test_centroids_k8_20['case_type'] = 'test'

train_test_appended_centroids_k8 = train_centroids_k8.append(test_centroids_k8_20)

train_test_appended_centroids_k8 = train_test_appended_centroids_k8.rename(columns={'Abstract_trim_2_string': 'Abstract_trim_2'})

##### Create dicksons word count frequency lists
##### When you re-read a csv you lose the list data type and so the literal_eval will restore it back to normal
for i in range(len(train_test_appended_centroids_k8['Abstract_trim_2'])):
    train_test_appended_centroids_k8['Abstract_trim_2'].values[i] = train_test_appended_centroids_k8['Abstract_trim_2'].values[i].split(' ')    

################################################################################## 
##################################################################################
#########  Find a way to do a for loop to run your function 
#########  for example for 6 cluster you have to do it 6 times 

#### k8 cluster models 

cluster = pd.unique(train_test_appended_centroids_k8['cluster'].tolist())
#train_test_appended_centroids_k8[(train_test_appended_centroids_k8['cluster'] == 'Cluster 0') & (train_test_appended_centroids_k8['case_type'] == 'test')]

list_cluster = []
for i in cluster:
      list_cluster.append(word_count_df(train_test_appended_centroids_k8[train_test_appended_centroids_k8['cluster'] == i]))  

list_cluster_filtered_cols = []
for i in range(len(list_cluster)):
   list_cluster_filtered_cols.append(list_cluster[i].loc[:,list_cluster[i].columns.str.startswith("IDF_")])

for df in range(len(list_cluster_filtered_cols)):
    list_cluster_filtered_cols[df] = list_cluster_filtered_cols[df].merge(train_test_appended_centroids_k8[['Lens ID','case_type','cluster']], how = 'left',on  = 'Lens ID')

list_cluster_train = []
list_cluser_test = []

for df in range(len(list_cluster_filtered_cols)):
    list_cluser_test.append(list_cluster_filtered_cols[df][(list_cluster_filtered_cols[df]['case_type'] == 'test')].set_index(["Lens ID"]))
    list_cluster_train.append(list_cluster_filtered_cols[df][(list_cluster_filtered_cols[df]['case_type'] == 'train')].set_index(["Lens ID"]))
      
#list_cluser_test.reset_index()
    
cluster_cosine = []
for i in range(len(list_cluster_filtered_cols)):
    if len(list_cluser_test[i]) > 0:
        cluster_cosine.append(pd.DataFrame(sk.metrics.pairwise.cosine_similarity(list_cluser_test[i].loc[:,list_cluser_test[i].columns.str.startswith("IDF_")],list_cluster_train[i].loc[:,list_cluster_train[i].columns.str.startswith("IDF_")]).transpose()))
    else:
        cluster_cosine.append(pd.DataFrame())

for i in range(len(cluster_cosine)):
    if len(list_cluser_test[i]) > 0:
        cluster_cosine[i].columns =  list_cluser_test[i].index
        cluster_cosine[i] = cluster_cosine[i].set_index(list_cluster_train[i].index)
        cluster_cosine[i].reset_index(inplace = True)
    else: next

base_table = []    
for i in range(len(list_cluster_train)):
        list_cluster_train[i].reset_index(inplace = True)
        base_table.append(list_cluster_train[i].loc[:,'Lens ID'])
        
base_table_df = pd.DataFrame(pd.concat(base_table))

for i in range(len(cluster_cosine)):
    if len(list_cluser_test[i]) > 0:    
        base_table_df = base_table_df.merge(cluster_cosine[i], how = 'left',on  = 'Lens ID')

cosine_table_df = base_table_df.fillna(0)

#### need to wait this one out for dickson to confirm whether he wants to rank the scores after each rows
#### should we create a massive table by unigrams, bygrams and clusters
#### this is going to be a big project now 
#### need to spot check it's the right cluster etc etc 
#### the cosine is computing the right lens ID etc etc

cosine_table_df.to_csv('C:/Users/andym/Desktop/Datafancy/Journal_managementNP/02-Python Scripts - Data Wrangling/Experiment_3_clustering/Final_datasets/final_data_clustering_K6_bigram.csv')


###############################################################################################
###############################################################################################
##### This part of the script be left for last so we can mostlikely create a massive dataset to
#####  run a ranking order on top of 


#test_columns = test_matrix_cosine_df.columns[test_matrix_cosine_df.columns != 'Lens ID']
#rank_matrix_cosine_df = [pd.DataFrame(test_matrix_cosine_df[test_columns].rank(method = 'first', ascending = False)) for i in test_columns][1] 

##list_cluster_train['Lens ID']
#pd.DataFrame(pd.concat(base_table))

#luster_cosine[1].loc[:,'Lens ID']
#cluster_cosine[1].index    
    
# cluster_cosine[1].reset_index(inplace = True)    
    
#    len(list_cluser_test)
#    cluster_cosine[i] = cluster_cosine[i].set_index(list_cluster_traini1].index)

#len(list_cluser_test[3])

#cluster_cosine[4].columns =  list_cluser_test[4].index
#cluster_cosine[1] = cluster_cosine[1].set_index(list_cluster_train[1].index)

#(list_cluser_test[1].pop('cluster')).index
#sk.metrics.pairwise.cosine_similarity(list_cluser_test[1],list_cluster_train[1])

#len(list_cluser_test[3])

#len(list_cluser_test)
#len(list_cluster_train)
#    list_cluster_filtered_cols[1].columns
# Needs spot checking
#test_matrix_cosine = cosine_similarity(x_train,x_test)
#test_matrix_cosine.shape

#pd.DataFrame(test_matrix_cosine).to_csv(r"C:\Users\andym\Desktop\Datafancy\Journal_managementNP\03-test_datasets\test_matrix.csv")
#test_matrix_cosine_df = pd.DataFrame(test_matrix_cosine)
#test_matrix_cosine_df = test_matrix_cosine_df.set_index(x_train.index)
#test_matrix_cosine_df.columns = x_test.index
