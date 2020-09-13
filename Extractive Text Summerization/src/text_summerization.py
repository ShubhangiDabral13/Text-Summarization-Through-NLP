#importing all the modules that are required
import numpy as np
import pandas as pd
import nltk
import networkx as nx
nltk.download('punkt') # one time execution
nltk.download('stopwords')
import re
import split_text_to_sentences
import sentence_preprocessing
import sentence2vector
import similarity_matrix_prep
import json


#reading the data from .csv file
df = pd.read_csv("tennis_articles.csv",encoding='latin1')

sentences = split_text_to_sentences.split_text(df["article_text"])
n = len(sentences)

#passing the sentences data to sentence_process function and preprocessing it.
clean_sentences = sentence_preprocessing.sentence_process(sentences)

#converting sentences to the vector from using GloVe
sentence_vectors  = sentence2vector.sent2vec(clean_sentences)

#creating the similarity matrix which contain similarity of each sentence with the other sentences.
sim_mat = similarity_matrix_prep.create_sim_mat(sentence_vectors,n)

nx_graph = nx.from_numpy_array(sim_mat)
#using the pagerank algorithm
scores = nx.pagerank(nx_graph)

#creating a list which consist of sentence and it's corresponding scores.
ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)


# Extract top 10 sentences as the summary
final_result = []
for i in range(10):
  final_result.append(ranked_sentences[i][1])


#and fianly saving the summary in summary.txt.
with open('summary.txt', 'w') as f:
    f.write(json.dumps(final_result))
