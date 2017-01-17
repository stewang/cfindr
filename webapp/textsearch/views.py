from django.shortcuts import render
#import sys
#sys.path.insert(0, '~/data')
#import CFindr

#from __future__ import print_function
#import argparse
#import pprint
import gensim
from django.conf import settings

from glove import Glove
from glove import Corpus

# Pre-load model
print('Loading pre-trained GloVe model')
glove=Glove.load_stanford(settings.BASE_DIR+'/textsearch/glove.model')

def search_text(input, wordToFind):
    wordToFind = wordToFind.lower()
    try:
	print('Querying for', wordToFind)
	gloveResults = glove.most_similar(wordToFind, number=20)
        gloveResults.insert(0, (wordToFind, 1.0))      # look for the word itself in addition to similar words

#	count = 0
	matchesList = []
	for word, closeness in gloveResults:
	    if closeness < 0.5:
		break
	    matchesList.extend([sentence.lstrip() + '.' for sentence in input.split('.') if word.lower() in sentence.lower()])
#	    count += 1
#	    if count >= 5:
#               break

	matchesList = list(set(matchesList))    # get rid of repeats
	return matchesList

    except Exception as e:
        print(e)
        return ['Error in func search_text(): ' + str(e)]

def index(request):
    context = {}
    try:
        inputStr = request.POST['input']
        keywordsStr = request.POST['query']
        if inputStr and keywordsStr:
	    context['input'] = inputStr
            context['query'] = keywordsStr
            
            resultsList = []
            keywordsList = keywordsStr.split()
            for keyword in keywordsList:
	        resultsList.extend(search_text(inputStr, keyword))
            resultsList = list(set(resultsList))        # get rid of repeats
            context['results'] = resultsList
	    print('Loaded resultsList into context.')
    except Exception as e:
        #print(e)
        context['results'] = ['Error in func index(): ' + str(e)]

    return render(request, 'textsearch/index.html', context)

