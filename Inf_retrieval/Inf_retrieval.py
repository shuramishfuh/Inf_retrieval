import nltk
def doIt(keyword):
    filtered = []
    tokenized = nltk.word_tokenize(keyword)

    for w in tokenized:
        if w not in stop_words:
            filtered.append(w)

    return tokenized, filtered