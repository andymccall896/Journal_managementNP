# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:20:50 2021

@author: andym
"""

check = sk.metrics.pairwise.cosine_similarity(list_cluser_test[0].loc[:,list_cluser_test[0].columns.str.startswith("IDF_")],
list_cluster_train[0].loc[:,list_cluster_train[0].columns.str.startswith("IDF_")]).transpose()

test = list_cluser_test[3]
train = list_cluster_train[3]
sk.metrics.pairwise.cosine_similarity(test.head(3).loc[:,test.columns.str.startswith("IDF_")],
train.head(8).loc[:,train.columns.str.startswith("IDF_")]).transpose()

g =list_cluster_train[0].loc[:,list_cluster_train[0].columns.str.startswith("IDF_")].index()

g = list_cluster_train[0].values('000-251-444-646-256')

list_cluster_filtered_cols[0].to_csv('C:/Users/andym/Desktop/Datafancy/Journal_managementNP/02-Python Scripts - Data Wrangling/Experiment_3_clustering/test_idf_frame.csv')