#Data wrangling package in Python 
import pandas as pd


#
import numpy as np
#Glob pythons filepath recognition 
import glob 
# Pythons package is the way in which it can interact with the operating system
import os
# natural language processing package 
import nltk 
import re
#R               | Pandas
#-------------------------------
#summary(df)     | df.describe()
#head(df)        | df.head()
#dim(df)         | df.shape
#slice(df, 1:10) | df.iloc[:9]
#os.chdir("C:/Users/andym/Desktop/Datafancy/Journal_managementNP/01-Raw_data/all_data")
#print(glob.glob("/home/adam/*.txt"))
#all_files = glob.glob(path + "/*.csv")
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer   
ps = PorterStemmer() 
porter = PorterStemmer()
lancaster=LancasterStemmer()
#proide a word to be stemmed
#print("Porter Stemmer")
#print(porter.stem("cats"))
#print(porter.stem("trouble"))
#print(porter.stem("troubling"))
#print(porter.stem("troubled"))
#print("Lancaster Stemmer")
#print(lancaster.stem("cats"))
#print(lancaster.stem("trouble"))
#print(lancaster.stem("troubling"))
#print(lancaster.stem("troubled"))
PYTHONPATH="c:/users/andym/anaconda3/lib/site-packages/":"${PYTHONPATH}"
export PYTHONPATH

C:\Users\andym\Anaconda3\envs\pyspark_env\site-packages

import sys; sys.path.insert(0, "C:/Users/andym/Anaconda3/envs/pyspark_env/site-packages")