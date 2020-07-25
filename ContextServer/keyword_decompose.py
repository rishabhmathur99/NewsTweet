import nltk 

def process_data(string):
    hashtags = []

    string = str(string)[2: -1]
    
    words = nltk.word_tokenize(string)

    words = [word for word in words if word.isalnum()]

    for index, word in enumerate(words):
        if word == '#' or word == '@':
            hashtags.append(words[index + 1])
            words.remove(word)
    return nltk.pos_tag(words), hashtags

def identifyNounPhrases(tagged):
    phrases = []
    phrase = ""
    for word in tagged:
        if word[1] == "NNP" or word[1] == "NNS" or word[1] == "NN" or word[1] == "NNPS":
            phrase = phrase + " " + word[0]
        else:
            phrases.append(phrase)
            phrase = ""

    phrases[:] = [x for x in phrases if x is not ""]

    return phrases

def get_keywords(string):
    tagged_data, hashtags = process_data(string)
    keywords = identifyNounPhrases(tagged_data)

    return keywords