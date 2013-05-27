import MapReduce
import sys
"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	friendA = record[0]
	friendB = record[1]
	mr.emit_intermediate(friendA, friendB)
	mr.emit_intermediate(friendB, friendA)

def reducer(key, list_of_values):
	#friendships = [set(item) for item in list_of_values]
	for item in list_of_values:
		if list_of_values.count(item) == 1:
		 	mr.emit((key,item))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)