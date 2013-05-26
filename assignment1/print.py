import urllib
import json
for x in xrange(1,10):
	response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page="+str(x))
	data = json.load(response)
	for tweet in data["results"]:
		print tweet["text"]