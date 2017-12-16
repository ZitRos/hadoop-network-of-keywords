import utils
import os
import csv

if not os.path.isfile('files_count.txt') \
   or not os.path.isfile('tf_df_output.txt') \
   or not os.path.isfile('file_name.txt'):
	print('Please, run shell script first: ./run_mapreduce.sh')
	exit(1)

print('Gathering a graph from computed TF-IDF values...')

ranks = {}
hvg = {}
max_rank = 0.0001
horizon = 20              # do not search in HVG behind the horizon
rank_threshold = 0.2      # filter less relevant words, ranked in relative range 0..1
commons = set()
line = []
text = []

with open('tf_df_output.txt') as f:
	content = f.readlines()
with open('files_count.txt') as f:
	documents = int(f.read())
with open('file_name.txt') as f:
	with open('texts/' + f.read().strip()) as f2:
		text = utils.get_normalized_words(f2.read())
tf_df_word = [x.strip().split() for x in content]

for [tf, df, word] in tf_df_word:
	ranks[word] = utils.tf_idf(int(tf), int(df), documents)
	if ranks[word] > max_rank:
		max_rank = ranks[word]

for word in text:
	rank = ranks[word] / max_rank
	line.append(rank)
	if rank < rank_threshold:
		commons.add(word)

all_words = set(text) - commons

def add_to_hvg(w1, w2):
	if w1 > w2:
		temp = w1
		w1 = w2
		w2 = temp
	if w1 not in hvg:
		hvg[w1] = {}
	hvg[w1][w2] = 0 if w2 not in hvg[w1] else hvg[w1][w2] + 1

limit = len(line)
for current in range(0, limit):
	if line[current] < rank_threshold:
		continue
	for left in reversed(range(max(0, current - horizon), max(0, current - 1))):
		if line[left] > line[current]:
			add_to_hvg(text[left], text[current])
			break
	for right in range(min(limit, current + 1), min(limit, current + horizon)):
		if line[right] > line[current]:
			add_to_hvg(text[right], text[current])
			break

with open("result.csv", "w") as f:
	writer = csv.writer(
		f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n'
	)
	matrix = [[""]]
	for word in all_words:
		matrix[0].append(word)

	for word1 in all_words:
		row = [word1]
		for word2 in all_words:
			if word1 > word2:
				wo1 = word2
				wo2 = word1
			else:
				wo1 = word1
				wo2 = word2
			row.append(hvg[wo1][wo2] if wo1 in hvg and wo2 in hvg[wo1] else 0)
		matrix.append(row)

	writer.writerows(matrix)

print('\nDone! See result in result.csv')
