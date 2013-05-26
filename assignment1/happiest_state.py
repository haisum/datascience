import sys,json

class State():
	def __init__(self, tweet, sentiment):
		self.tweet = tweet
		self.sentiment = sentiment
		self.states =	{
		    'AK': 'Alaska',
		    'AL': 'Alabama',
		    'AR': 'Arkansas',
		    'AS': 'American Samoa',
		    'AZ': 'Arizona',
		    'CA': 'California',
		    'CO': 'Colorado',
		    'CT': 'Connecticut',
		    'DC': 'District of Columbia',
		    'DE': 'Delaware',
		    'FL': 'Florida',
		    'GA': 'Georgia',
		    'GU': 'Guam',
		    'HI': 'Hawaii',
		    'IA': 'Iowa',
		    'ID': 'Idaho',
		    'IL': 'Illinois',
		    'IN': 'Indiana',
		    'KS': 'Kansas',
		    'KY': 'Kentucky',
		    'LA': 'Louisiana',
		    'MA': 'Massachusetts',
		    'MD': 'Maryland',
		    'ME': 'Maine',
		    'MI': 'Michigan',
		    'MN': 'Minnesota',
		    'MO': 'Missouri',
		    'MP': 'Northern Mariana Islands',
		    'MS': 'Mississippi',
		    'MT': 'Montana',
		    'NA': 'National',
		    'NC': 'North Carolina',
		    'ND': 'North Dakota',
		    'NE': 'Nebraska',
		    'NH': 'New Hampshire',
		    'NJ': 'New Jersey',
		    'NM': 'New Mexico',
		    'NV': 'Nevada',
		    'NY': 'New York',
		    'OH': 'Ohio',
		    'OK': 'Oklahoma',
		    'OR': 'Oregon',
		    'PA': 'Pennsylvania',
		    'PR': 'Puerto Rico',
		    'RI': 'Rhode Island',
		    'SC': 'South Carolina',
		    'SD': 'South Dakota',
		    'TN': 'Tennessee',
		    'TX': 'Texas',
		    'UT': 'Utah',
		    'VA': 'Virginia',
		    'VI': 'Virgin Islands',
		    'VT': 'Vermont',
		    'WA': 'Washington',
		    'WI': 'Wisconsin',
		    'WV': 'West Virginia',
		    'WY': 'Wyoming'
		}

	def scores(self):
		state_scores = {}
		for code,name in self.states.iteritems():
			for index in  xrange(0,len(self.tweet.List)):
				place = self.tweet.place(index)
				if place != "" and place.find(", " + code) != -1 or place.find(name) != -1:
					score = self.sentiment.score(self.tweet.words(index))
					if code in state_scores:
						state_scores[code] = state_scores[code] + score
					else:
						state_scores[code] = score
		return state_scores

	def happiest(self):
		state_scores = self.scores()
		max_key = max(state_scores.iterkeys(), key=lambda k: state_scores[k])
		return max_key

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

def main():
	tweet = Tweet(sys.argv[2])
	sentiment = Sentiment(sys.argv[1])
	state = State(tweet, sentiment)
	#print tweet.place(2)
	print state.happiest()
		

if __name__ == "__main__":
	main()