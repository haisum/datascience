import sys,json,re

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

	def term_frequencies(self):
		frequencies ={"total" : 0 , "terms" : {}}
		for index, tweet in enumerate(self.List):
			words = self.words(index)
			for word in words:
				frequencies["total"] = frequencies["total"] + 1
				if word in frequencies["terms"]:
					frequencies["terms"][word] = frequencies["terms"][word] + 1
				else:
					frequencies["terms"][word] = 1
		return frequencies

def main():
	tweet = Tweet(sys.argv[1])
	term_fr = tweet.term_frequencies()
	for term, frequency in term_fr["terms"].iteritems():
		#make sure it's a word
		if re.match('^[\w-]+$', term):
			print term + " " + str(float(frequency)/term_fr["total"])	

if __name__ == "__main__":
	main()