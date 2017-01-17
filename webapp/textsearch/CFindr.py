from __future__ import print_function
import argparse
import pprint
import gensim

from glove import Glove
from glove import Corpus

def search_text(input, wordToFind):
    try:
        print('Loading pre-trained GloVe model')
	glove = Glove.load_stanford('glove.model')
	print('Querying for', wordToFind)
	results = glove.most_similar(wordToFind, number=20)

	count = 0
	matchesList = []
	for word, closeness in results:
		if closeness < 0.5:
			break
		matchesList.extend([sentence.lstrip() + '.' for sentence in input.split('.') if word in sentence or wordToFind in sentence])
		matchesList = list(set(matchesList))
		count += 1
		if count >= 5:
			break

	return matchesList

    except Exception as e:
        print(e)
        return ['Error']

#print(search_text('This is a girl. This is a boy. I like octopi. I am a baby. I like girls. You are a woman. I am teenage.', 'girl'))
