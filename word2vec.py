from gensim.models import Word2Vec

class MySentence(object):
	def __iter__(self):
		for lin in open('/home/geek/codes/nosql/lda/mycorpus.txt','r'):
			yield lin.lower().split(' ')

sentences = MySentence()
model = Word2Vec(sentences,min_count=1)
print model['computer']
