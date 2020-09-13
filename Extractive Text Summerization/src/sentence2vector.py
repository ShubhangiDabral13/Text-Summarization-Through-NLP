import numpy as np

# function to extract the words embeddings or word vectors
def sent2vec(clean_sentences):
    word_embeddings = {}
    f = open('glove.6B.100d.txt', encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        word_embeddings[word] = coefs
    f.close()

    #et’s create vectors for our sentences.
    """
    We will first fetch vectors (each of size 100 elements) for the constituent words in a sentence and then take
    mean/average of those vectors to arrive at a consolidated vector for the sentence.
    """

    sentence_vectors = []
    for i in clean_sentences:
        if len(i) != 0:
            v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
        else:
            v = np.zeros((100,))
        sentence_vectors.append(v)

    return sentence_vectors
