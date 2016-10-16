import nltk
from nltk.sentiment import SentimentAnalyzer
from nltk.tokenize import sent_tokenize
import sys
import os
import docx

def demo_liu_hu_lexicon(sentence, plot=False):
    """
    Basic example of sentiment classification using Liu and Hu opinion lexicon.
    This function simply counts the number of positive, negative and neutral words
    in the sentence and classifies it depending on which polarity is more represented.
    Words that do not appear in the lexicon are considered as neutral.

    :param sentence: a sentence whose polarity has to be classified.
    :param plot: if True, plot a visual representation of the sentence polarity.
    """
    from nltk.corpus import opinion_lexicon
    from nltk.tokenize import treebank

    tokenizer = treebank.TreebankWordTokenizer()
    pos_words = 0
    neg_words = 0
    tokenized_sent = [word.lower() for word in tokenizer.tokenize(sentence)]

    x = list(range(len(tokenized_sent))) # x axis for the plot
    y = []

    for word in tokenized_sent:
        if word in opinion_lexicon.positive():
            pos_words += 1
            y.append(1) # positive
        elif word in opinion_lexicon.negative():
            neg_words += 1
            y.append(-1) # negative
        else:
            y.append(0) # neutral

    if pos_words > neg_words:
        return('Positive')
    elif pos_words < neg_words:
        return('Negative')
    elif pos_words == neg_words:
        return('Neutral')

    if plot == True:
        _show_plot(x, y, x_labels=tokenized_sent, y_labels=['Negative', 'Neutral', 'Positive'])

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

#txt = open(raw_input("Type in a file name to open: "))
txt = getText(raw_input("Type in a file name to open: "))

sentences = sent_tokenize(txt)

print sentences

num_sentences = len(sentences)

print "There are %d sentences in the article." % num_sentences

#print "Here are your sentences: %r" % sentences
# For articles with too many sentences, too many lines to print.

i = 0
pos = 0
neg = 0

while i < num_sentences:
    #sys.stdout = open(os.devnull, "w") # stops the nltk function from printing
    sentence = sentences[i]

    result = demo_liu_hu_lexicon(sentence, plot=False)
    #sys.stdout = sys.__stdout__
    #print result
    if result == "Positive":
        pos += 1
    if result == "Negative":
        neg += 1
    i += 1
    #sys.stdout = sys.__stdout__ # allows future printing

print "There are %d positive sentences in the article." % pos
print "There are %d negative sentences in the article." % neg

if pos > neg:
    print "The tone of this article is positive!"
if neg > pos:
    print "The tone of this article is negative!"
if neg == pos:
    print "The tone of this article is neutral!"
