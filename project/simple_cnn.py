from nltk import word_tokenize
from gensim import corpora
from wordcloud import WordCloud


def load_dataset():
    with open(file='alice.txt', mode='r', errors='ignore', encoding='utf-8') as f:
        document = []
        lines = f.readlines()
        for line in lines:
            value = clear_data(line)
            if value != '':
                for str in word_tokenize(value):
                    if str == 'CHAPTER':
                        break
                    else:
                        document.append(str.lower())
        return document


def clear_data(str):
    value = str.replace('\ufeff', '').replace('\n', '')
    return value


document = load_dataset()


def word_to_integer(document):
    dict = corpora.Dictionary([document])
    dict.save_as_text('dict.txt')
    dict_set =dict.token2id
    values = []
    for word in document:
        values.append(dict_set[word])
    return values


word_to_integer(document)


def show_word_cloud(document):
    left_word = [',', '.', '?', '!', ';', ':', '\'', '(', ')']
    dict = corpora.Dictionary([document])
    words_set = dict.doc2bow(document)

    words, frequences = [], []
    for item in words_set:
        key = item[0]
        frequence = item[1]
        word = dict.get(key=key)
        if word not in left_word:
            words.append(word)
            frequences.append(frequence)

    word_cloud = WordCloud(width=1000, height=620)
    word_cloud.generate_from_frequencies(frequences)
    word_cloud.to_file('Alice.png')


show_word_cloud(document)