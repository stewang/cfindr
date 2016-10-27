from gensim import corpora, models, similarities
dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
corpus = corpora.MmCorpus('/tmp/deerwester.mm') # comes from the first tutorial, "From strings to vectors"
print(corpus)

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)



index = similarities.MatrixSimilarity(lsi[corpus]) # transform corpus to LSI space and index it
#keep index
index.save('/tmp/deerwester.index')
index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')

#outputs documents and relevance to doc variable. Purely based on words appeareance
doc = "Human computer interaction"
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow] # convert the query to LSI space
sims = index[vec_lsi] # perform a similarity query against the corpus
print(list(enumerate(sims))) # print (document_number, document_similarity) 2-tuples

#Outputs by descending order of relevancy
sims = sorted(enumerate(sims), key=lambda item: -item[1])
print(sims)