# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 18:20:59 2021

@author: andym
I will concatenate the cluster dataframe into one table and do a rank for each column

"""
#Data wrangling package in Python 
import pandas as pd
import numpy as np
#Glob pythons filepath recognition 
import glob 
# Pythons package is the way in which it can interact with the operating system
import os
# natural language processing package 
import nltk 
import re
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer   


cosine_dataframe = pd.read_excel(r'C:/Users/andym/Desktop/Datafancy/Journal_managementNP/04-final_datatsets/cosine_journal_check_df_final_20.xlsx').dropna()
column_order = []
column_order.append('Unnamed: 0')
column_order.append('Lens ID')
column_order.extend(cosine_dataframe["Lens ID_Test "].tolist())

path =r'C:\Users\andym\Desktop\Datafancy\Journal_managementNP\02-Python Scripts - Data Wrangling\Experiment_3_clustering\Final_datasets'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df['file_name'] = filename
    li.append(df)
    
    
for i in range(len(li)):    
    li[i] = li[i].loc[:,column_order]    
    
full_cluster_table = pd.concat(li)

del full_cluster_table['Unnamed: 0']

full_cluster_table = full_cluster_table.set_index('Lens ID')

test_columns = full_cluster_table.columns[full_cluster_table.columns != 'Lens ID']


rank_matrix_cosine_df = [pd.DataFrame(full_cluster_table[test_columns].rank(method = 'first', ascending = False)) for i in test_columns][1] 

rank_matrix_cosine_df['Lens ID'] = full_cluster_table.index
lst = []
rank_cols = rank_matrix_cosine_df.columns

for cols in rank_cols:
    lst.append(rank_matrix_cosine_df[['Lens ID',cols]].loc[rank_matrix_cosine_df[cols] == 1])
    
    
del lst[20]
rank_matrix_cosine_df_final = pd.concat(lst).fillna(0)

del lst[20]
rank_matrix_cosine_df_final =rank_matrix_cosine_df_final.reset_index


dsada = rank_matrix_cosine_df_final
full_cluster_table['Lens ID'] = full_cluster_table.index



full_cluster_table.to_csv(r'C:/Users/andym/Desktop/Datafancy/Journal_managementNP/02-Python Scripts - Data Wrangling/Experiment_3_clustering/Datasets/dsadasd.csv')
rank_matrix_cosine_df_final.to_csv(r'C:/Users/andym/Desktop/Datafancy/Journal_managementNP/02-Python Scripts - Data Wrangling/Experiment_3_clustering/rank_cluster_cosine_df_final.csv')

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
