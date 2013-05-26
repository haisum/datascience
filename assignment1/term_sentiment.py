import sys,json

class Tweet():
	def __init__(self, tweet_file):
		file = open(tweet_file)
		items = file.readlines()
		tweetList = []
		for item in items:
			tweet = json.loads(item)
			if "text" in tweet:
				tweetList.append(tweet)
		self.List = tweetList

	def words(self, index):
		return self.List[index]["text"].split(" ")

class Sentiment():
	def __init__(self, sentiment_file):
		lines = open(sentiment_file)
		scores = {} # initialize an empty dictionary
		for line in lines:
		  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		  scores[term] = int(score)  # Convert the score to an integer.
		self.scores = scores

	def score(self, words):
		score = 0
		for word in words:
			if word in self.scores:
				score = score + self.scores[word]
		return score

	def avg_score(self, words):
		score = 0
		scoring_words = 0
		for word in words:
			if word in self.scores:
				score = score + self.scores[word]
				scoring_words = scoring_words + 1
		try:
			return float(score)/scoring_words
		except ZeroDivisionError:
			return 0

def main():
	tweet = Tweet(sys.argv[2])
	sentiment = Sentiment(sys.argv[1])

	for index in xrange(0, len(tweet.List)):
		words = tweet.words(index)
		avg_score = sentiment.avg_score(words)
		for word in words:
			print word + " " + str(avg_score)

if __name__ == "__main__":
	main()