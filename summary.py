from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest

import urllib2
from bs4 import BeautifulSoup


class FrequencySummarizer:
    def __init__(self, min_cut=0.1, max_cut=0.9):
        self._min_cut = min_cut
        self._max_cut = max_cut
        self._stopwords = set(stopwords.words('english') + list(punctuation))
        # print self
        # print min_cut
        # print max_cut

    def _compute_frequencies(self, word_sent):
        freq = defaultdict(int)
        for sentence in word_sent:
            for word in sentence:
                if word not in self._stopwords:
                    freq[word] += 1
        max_freq = float(max(freq.values()))
        for word in freq.keys():
            freq[word] = freq[word] / max_freq
            if freq[word] >= self._max_cut or freq[word] <= self._min_cut:
                del freq[word]
        return freq

    def summarize(self, text, n):
        sents = sent_tokenize(text)
        assert n <= len(sents)
        word_sent = [word_tokenize(s.lower()) for s in sents]
        self._freq = self._compute_frequencies(word_sent)
        rankings = defaultdict(int)
        for i, sent in enumerate(word_sent):
            for word in sent:
                if word in self._freq:
                    # print self._freq[word]
                    # rankings = rankings + self._freq[word]
                    rankings[i] += self._freq[word]
                    # print rankings
                    # sent_idx = nlargest(n, rankings[i], key=rankings.get)
                    sent_idx = nlargest(n, rankings, key=rankings.get)
                    return [sents[j] for j in sent_idx]


############################################################################################################################################################

url = "http://timesofindia.indiatimes.com/india/data-protection-regime-will-be-in-place-by-diwali-centre-tells-sc/articleshow/58250402.cms"


def get_only_text_from_post(url):
    page = urllib2.urlopen(url).read().decode('utf8')
    # print page //TODO: <div class="Normal">
    soup = BeautifulSoup(page)
    # print soup
    text = ' '.join(map(lambda p: p.text, soup.find_all('div', {"class": "Normal"})))
    # print text
    # print soup.title.text
    return soup.title.text, text


textFromURL = get_only_text_from_post(url)
# print textFromURL[0]
# print textFromURL[1]

fs = FrequencySummarizer()

summary = fs.summarize(textFromURL[1], 3)

print "********** SUMMARY **********"
print summary
