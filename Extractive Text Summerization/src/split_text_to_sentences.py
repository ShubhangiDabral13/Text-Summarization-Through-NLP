
#we will split the text into different sentence and then append it to the list.
def split_text(text):
    """
    param text: it is the plain text
    return a list which consist of sentence present in text.
    """
    from nltk.tokenize import sent_tokenize
    sentences = []
    for s in text:
        sentences.append(sent_tokenize(s))

     # flatten list
    sentences = [y for x in sentences for y in x]
    # return the sentences after beind sentence tokenized
    return sentences
