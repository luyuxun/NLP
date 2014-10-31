# coding=utf-8
from nltk.corpus import wordnet as wn
file = open('RG.csv')
dict_score = [[0]*2]*100 #2维数组
i = 0
for line in file:
	#这个循环中我们将打分和词对分离出来
	dict_score[i] = line.split(',')
	i = i + 1
#i记录的是有多少行数据
#dict_score[k][0]是词对
#dict_score[k][1]是打分
for k in range(i):
	#将词拆出来,e.g. 'human-people' -> ['human','people']
	single_word = dict_score[k][0].split('-')
	noun_synsets1 = wn.synsets(single_word[0],pos=wn.NOUN)
        noun_synsets2 = wn.synsets(single_word[1],pos=wn.NOUN)
        #打印第一个词
	print single_word[0] + ':'
	#打印第一个词的名词的所有synset,形式例如:Synset['cat.n.01']
	#print 'synset is',noun_synsets1
        for s1 in noun_synsets1:
		#打印Synset['cat.n.01']的所有同义词
                for lemma1 in s1.lemmas():
			print str(lemma1.name()),
	print
	print single_word[1] + ':'
	#print 'synset is',noun_synsets2
	for s2 in noun_synsets2:
		for lemma2 in s2.lemmas():
			print str(lemma2.name()),
	print
