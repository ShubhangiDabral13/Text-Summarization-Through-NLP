
## Extractive Text Summerization 

* [**Overview**](https://github.com/ShubhangiDabral13/Text-Summerization-Through-NLP/tree/master/Extractive%20Text%20Summerization#Overview)
* [**TextRank Algorithm**](https://github.com/ShubhangiDabral13/Text-Summerization-Through-NLP/tree/master/Extractive%20Text%20Summerization#TextRank-Algorithm)
* [**About Project**](https://github.com/ShubhangiDabral13/Text-Summerization-Through-NLP/tree/master/Extractive%20Text%20Summerization#About-Project)
* [**References**](https://github.com/ShubhangiDabral13/Text-Summerization-Through-NLP/tree/master/Extractive%20Text%20Summerization#References)

### Overview

Extractive Summarization: These methods rely on extracting several parts, such as phrases and sentences, from a piece of text and stack them together to create a summary. Therefore, identifying the right sentences for summarization is of utmost importance in an extractive method.

![1](https://user-images.githubusercontent.com/44902363/93118722-535d0880-f6de-11ea-896f-be517bfeda20.png)


In this projects i have used **TextRank Algorithm.**

### TextRank Algorithm 

TextRank is an extractive and unsupervised text summarization technique. Let’s take a look at the flow of the TextRank algorithm that we will be following:

![block_3](https://user-images.githubusercontent.com/44902363/93119003-b8186300-f6de-11ea-8139-551664f13944.png)

* The first step would be to concatenate all the text contained in the articles
* Then split the text into individual sentences
* In the next step, we will find vector representation (word embeddings) for each and every sentence
* Similarities between sentence vectors are then calculated and stored in a matrix
* The similarity matrix is then converted into a graph, with sentences as vertices and similarity scores as edges, for sentence rank calculation
* Finally, a certain number of top-ranked sentences form the final summary

### About Project 

You can download the dataset we’ll be using from [here](https://drive.google.com/file/d/1HPShiXSrHMNlfcMZn-WFYjoftitOH9fJ/view).

Steps for the project :
* **Import Required Libraries, read the data and ispect the data** 
* **Split Text into Sentences**: The next step is to break the text into individual sentences. We will use the sent_tokenize( ) function of the nltk library to do this.
* **Text Preprocessing**: We will make our textual data noise-free as much as possible by removing stop words or any special characters.
* **Vector Representation of Sentences** : GloVe word embeddings are vector representation of words. These word embeddings will be used to create vectors for our sentences. We could have also used the Bag-of-Words or TF-IDF approaches to create features for our sentences, but these methods ignore the order of the words (and the number of features is usually pretty large).
You can download it at [**GloVe**](https://nlp.stanford.edu/data/glove.6B.zip)
* **Similarity Matrix Preparation** : The next step is to find similarities between the sentences, and we will use the cosine similarity approach for this challenge. We will create an empty similarity matrix for this task and populate it with cosine similarities of the sentences.
* **Applying PageRank Algorithm** : Before proceeding further, let’s convert the similarity matrix sim_mat into a graph. The nodes of this graph will represent the sentences and the edges will represent the similarity scores between the sentences. On this graph, we will apply the PageRank algorithm to arrive at the sentence rankings.
* **Summary Extraction** : Finally, it’s time to extract the top N sentences based on their rankings for summary generation.

### References
* [Text Summarisation with Gensim (TextRank Algorithm)](https://medium.com/@shivangisareen/text-summarisation-with-gensim-textrank-46bbb3401289)
* [Introduction to text summerization](https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/?utm_campaign=News&utm_medium=Community&utm_source=DataCamp.com)





#### Shubhangi Dabral (ShubhangiDabral13)
<a href="https://twitter.com/Shubhi_Dabral"><img 
src="https://news.wjct.org/sites/wjct/files/styles/medium/public/201407/v65oai7fxn47qv9nectx.png" align="left" height="50" width="50" ></a>
<a href="https://www.linkedin.com/in/shubhangi-dabral-b79705145/"><img src="https://cdn2.iconfinder.com/data/icons/simple-social-media-shadow/512/14-512.png" align="left" height="60" width="60" ></a>



