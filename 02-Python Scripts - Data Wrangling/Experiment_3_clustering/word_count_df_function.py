# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:39:02 2021
you can try and mimic some fake data with a few records to spot check this functions 
@author: andym
"""

def word_count_df(testing_loop):

    from collections import Counter
    import numpy as np

    def getUniqueWords(allWords):
        uniqueWords = [] 
        for i in allWords:
            if not i in uniqueWords:
                uniqueWords.append(i)
        return uniqueWords

    testing_loop_long = testing_loop
    testing_loop_long['Abstract_trim_2_distinct'] = testing_loop_long['Abstract_trim_2']
    for id,i in enumerate(testing_loop_long['Abstract_trim_2']):
        testing_loop_long['Abstract_trim_2_distinct'].iloc[id] = getUniqueWords(i)
        
    testing_loop_long = testing_loop_long[testing_loop_long.astype(str)['Abstract_trim_2_distinct'] != '[]']
    testing_loop = testing_loop[testing_loop.astype(str)['Abstract_trim_2_distinct'] != '[]']    

    testing_loop['abstract_counts'] = [Counter(x).most_common() for x in testing_loop['Abstract_trim_2']]

    testing_loop = testing_loop[testing_loop.astype(str)['abstract_counts'] != '[]']

    testing_loop_long = testing_loop[['Lens ID','Abstract_trim_2_distinct','Abstract_trim_2']].explode('Abstract_trim_2_distinct')

    testing_loop_long['abstract_counts_unlist'] = [val for sublist in testing_loop['abstract_counts'] for val in sublist]

#pd.DataFrame(testing_loop['abstract_counts_unlist'])
#### Unzip the individual tuples and covert into seperate columns
#testing_loop_long['Word'] = testing_loop_long['Abstract_trim_2_distinct']
#testing_loop_long['Count'] = testing_loop_long['Abstract_trim_2_distinct']
    testing_loop_long['Word'], testing_loop_long['Count'] = zip(*testing_loop_long['abstract_counts_unlist'])
    testing_loop_long['Binary_count'] = 1

    testing_loop_long["Total_words_in_abstract"] = testing_loop_long['Abstract_trim_2']
    for id,i in enumerate(testing_loop_long['Abstract_trim_2']):
        testing_loop_long["Total_words_in_abstract"].iloc[id] = len(testing_loop_long['Abstract_trim_2'].iloc[id])
    testing_loop_long['Cal_Term_Freq_TF'] =  (testing_loop_long['Count']/testing_loop_long["Total_words_in_abstract"])
    
    testing_loop_long_Count = testing_loop_long[['Lens ID','Word','Count']].pivot_table(index = 'Lens ID',columns = 'Word' , values = 'Count').fillna(0).add_prefix('Count_')   
    testing_loop_long_Count = pd.DataFrame(testing_loop_long_Count.to_records())

    testing_loop_long_TF = testing_loop_long[['Lens ID','Word','Cal_Term_Freq_TF']].pivot_table(index = 'Lens ID',columns = 'Word' , values = 'Cal_Term_Freq_TF',aggfunc = np.sum).fillna(0).add_prefix('TF_')      
    testing_loop_long_TF = pd.DataFrame(testing_loop_long_TF.to_records()) 

    testing_loop_long_Binary = testing_loop_long[['Lens ID','Word','Binary_count']].pivot_table(index = 'Lens ID',columns = 'Word' , values = 'Binary_count').fillna(0).add_prefix('Binary_') 
    testing_loop_long_Binary = pd.DataFrame(testing_loop_long_Binary.to_records()) 

    testing_loop_long['abstract_concat_list'] = testing_loop_long['Abstract_trim_2']
    for i in range(len(testing_loop_long['Abstract_trim_2'])):
        testing_loop_long['abstract_concat_list'].values[i] = testing_loop['Abstract_trim_2'].tolist()
    
    testing_loop_long['dsad'] = testing_loop_long['abstract_concat_list']
    for id1,o in enumerate(testing_loop_long['abstract_concat_list']):
        for id2,i in enumerate(o):
            testing_loop_long['dsad'].iloc[id1][id2] = [i for i in testing_loop_long['abstract_concat_list'].iloc[id1][id2] if i == testing_loop_long['Word'].values[id1]] 

    for id,i in enumerate(testing_loop_long['dsad']):
        testing_loop_long['dsad'].values[id] = [x for x in testing_loop_long['dsad'].values[id] if x != []]        

    testing_loop_long['times_mentioned_in_abstracts'] = [len(x) for x in testing_loop_long['dsad']]   
    testing_loop_long['Total_number_abstracts'] = len(testing_loop["Abstract_trim_2"])       
    testing_loop_long['Cal_Inverse_Document_Freq_IDF'] = np.log10(testing_loop_long['Total_number_abstracts']/testing_loop_long['times_mentioned_in_abstracts'])

    testing_loop_long_IDF = testing_loop_long[['Lens ID','Word','Cal_Inverse_Document_Freq_IDF']].pivot_table(index = 'Lens ID',columns = 'Word' , values = 'Cal_Inverse_Document_Freq_IDF').fillna(0).add_prefix('IDF_')  
    testing_loop_long_IDF = pd.DataFrame(testing_loop_long_IDF.to_records()) 

    testing_loop_wide = testing_loop_long_IDF.set_index('Lens ID').join(testing_loop_long_TF.set_index('Lens ID')).join(testing_loop_long_Count.set_index('Lens ID')).join(testing_loop_long_Binary.set_index('Lens ID'))

    return testing_loop_wide
