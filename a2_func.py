from functools import reduce
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter

## task 1

def mapper(x):
    return int((x[0] >= x[1]) & (x[0] <= x[2]))

def reducer(x, y):
    return x + y

def chunks_mapper(chunk):
    mapped_chunk = map(mapper, chunk) 
    return reduce(reducer, mapped_chunk)


## task 2

def one_book_word_count(filename):
    print(filename)
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    start_idx = text.find('***') + text[text.find('***') + 3 :].find('***') + 6
    end_idx = text.find('*** END')
    text = text[start_idx:end_idx].replace('\n',' ').replace('.',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('?',
            ' ').replace('!',' ').replace('"',' ').replace("—"," ").replace('_',' ').replace('[',' ').replace(']',' ').replace('(',
            ' ').replace(')',' ').replace('0',' ').replace('1',' ').replace('2',' ').replace('3',' ').replace('4',' ').replace('5',
            ' ').replace('6',' ').replace('7',' ').replace('8',' ').replace('9',' ').replace('-',' ').replace("'",' ').lower()
    text_tokenized = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    stop_words = stopwords.words('english')
    text_stem = [lemmatizer.lemmatize(item) for item in text_tokenized if ((len(lemmatizer.lemmatize(item)) > 1) & (item not in stop_words))]
    dict_of_words = dict(Counter(text_stem))
    
    return dict_of_words

def add_word_dicts(dict1, dict2):
    for k, v in dict2.items():
        if k in dict1.keys():
            dict1[k] = dict1[k] + v
        else:
            dict1[k] = v
    return dict1


## task 4

def make_pairs(row):
    return (row[0], (row[3], row[1], row[2]))

def first_multiply(list_of_tuples):
    pairs = []
    for tuple1 in list_of_tuples:
        for tuple2 in list_of_tuples:
            if (tuple1[0] == 'A') & (tuple2[0] == 'B'):
                pairs.append([(tuple1[1], tuple2[1]), tuple1[2]*tuple2[2]])
    return pairs

def sum_up(first, second):
    summed = []
    for i in range(len(first)):
        summed.append([first[i][0], first[i][1] + second[i][1]])
    return(summed)


## task 3

def nth_pi_digit(n):
    x = (4 * S(1, n-1) - 2 * S(4, n-1) - S(5, n-1) - S(6, n-1)) % 1.0
    return '{:x}'.format(int(x * 16))


def make_pi(a, b):
    return "{a}{b}".format(a=a, b=b)


def S(j, n):
    s1 = 0.0
    for k in range(n+1):
        s1 = (s1 + pow(16, n - k, 8 * k + j) / (8 * k + j)) % 1.0

    s2 = 0.0
    k = n + 1
    while True:
        temp = s2 + pow(16, n - k) / (8 * k + j)
        # Iterate until sum2 no longer changes
        if s2 == temp:
            break
        else:
            s2 = temp
        k += 1
    return s1 + s2