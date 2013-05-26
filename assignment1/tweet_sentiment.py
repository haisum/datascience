import sys
import json


def sentiments(sent_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	return scores

def tweets(tweet_file):
	items = tweet_file.readlines()
	tweetList = []
	for item in items:
		tweet = json.loads(item)
		if 'text' in tweet.keys():
			tweetList.append(tweet["text"].split(" "))
		else:
			tweetList.append([])
	return tweetList

def score(words, sentiments):
	score = 0
	for word in words:
		if word in sentiments:
			score = score + sentiments[word]
	return score

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	scores = sentiments(sent_file)
	wordList = tweets(tweet_file)
	for words in wordList:
		print str(score(words, scores))

if __name__ == '__main__':
	main()
