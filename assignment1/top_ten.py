import sys,json,operator

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

	def place(self, index):
		if "place" in self.List[index] and self.List[index]["place"] != None:
			return self.List[index]["place"]["full_name"]
		else:
			return ""

	def hash_tags(self, index):
		hashes = []
		if "entities" in self.List[index]:
			for hash in self.List[index]["entities"]["hashtags"]:
				hashes.append(hash["text"])
		return hashes

	def top_hash_tags(self):
		tag_dict = dict()
		for index in xrange(0, len(self.List)):
			tags = self.hash_tags(index)
			for tag in tags:
				if tag in tag_dict:
					tag_dict[tag] = tag_dict[tag] + 1
				else:
					tag_dict[tag] = 1
		sorted_hashes = sorted(tag_dict.iteritems(), key=operator.itemgetter(1),reverse=True)
		return sorted_hashes

def main():
	tweet = Tweet(sys.argv[1])
	top_hash_tags = tweet.top_hash_tags()
	for key,value in top_hash_tags[0:10]:
		print key + " " + str(float(value))
		

if __name__ == "__main__":
	main()