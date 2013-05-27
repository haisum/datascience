import MapReduce
import sys
import copy
"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    table = record[0]
    order_id = record[1]
    for field in record:
      mr.emit_intermediate(order_id, field)

def reducer(order_id, list_of_values):
    order = list_of_values[0:10]
    for index in xrange(10, len(list_of_values), 17):
      record = copy.deepcopy(order) + list_of_values[index:index+17]
      mr.emit(record)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)