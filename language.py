import sys

sys.path.append("/Users/ajinkyapuar/anaconda/lib/python2.7/site-packages/")

# for path in sys.path:
#     print path

import nltk
import matplotlib

from nltk.book import *

# text1.concordance("monstrous")

# text2.concordance("monstrous")

# text2.similar("monstrous")

# text2.common_contexts(["monstrous","very"])

# text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# text1.dispersion_plot(["happy", "sad"])

# text2.dispersion_plot(["happy", "sad"])

########################################################################################################################


from nltk.tokenize import word_tokenize, sent_tokenize

# text = "Mary had a little lamb. Her fleece was white as snow"
#
# sents = sent_tokenize(text)
#
# print sents
#
# words = [word_tokenize(sent) for sent in sents]
#
# print(words)

########################################################################################################################


from nltk.corpus import stopwords

from string import punctuation

#
# customStopWords = set(stopwords.words('english') + list(punctuation))
#
# wordsWOStopwords = [word for word in word_tokenize(text) if word not in customStopWords]
#
# print(wordsWOStopwords)

########################################################################################################################


text2 = "Mary closed on closing night when she was in the mood to close."

from nltk.stem.lancaster import LancasterStemmer

# st = LancasterStemmer()
#
# stemmedWords = [st.stem(word) for word in word_tokenize(text2)]
#
# print (stemmedWords)
#
# print nltk.pos_tag(word_tokenize(text2))

########################################################################################################################

