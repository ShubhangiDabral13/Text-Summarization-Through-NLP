def sentence_process(sentences):
    """
    param sentences: sentence is passed to it.
    return the preprocessed sentences
    """
    #importing the modules that are required
    import pandas as pd
    from nltk.corpus import stopwords

    # remove punctuations, numbers and special characters
    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")

    # make alphabets lowercase
    clean_sentences = [s.lower() for s in clean_sentences]

    stop_words = stopwords.words('english')

    # function to remove stopwords
    def remove_stopwords(sen):
        sen_new = " ".join([i for i in sen if i not in stop_words])
        return sen_new

    # removing less important and more frequent words like the,and etc (also called stop words) from the sentences
    clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

    return clean_sentences
