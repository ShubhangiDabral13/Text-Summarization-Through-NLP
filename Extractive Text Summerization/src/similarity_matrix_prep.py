# similarity matrix
import numpy as np

# function to find similarities between the sentences, and we will use the cosine similarity approach
def create_sim_mat(sentence_vectors,n):

    """
    param sentence_vectors: consist of sentence in a vector form
    param n: consist of number of sentences
    return sim_mat which is a matrix that represent the similarity between each sentence with respect to others
    """
    sim_mat = np.zeros([n,n])

    # importing Cosine Similarity
    from sklearn.metrics.pairwise import cosine_similarity

    # Initialize the matrix with cosine similarity scores.
    for i in range(n):
        for j in range(n):
            if i != j:
                sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]

    return sim_mat
