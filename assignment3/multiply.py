import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

K = [0,1,2,3,4]

def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]

    if matrix == "a":
      for k in K:
        mr.emit_intermediate((i,k), {str(i)+","+str(j):value})
    elif matrix == "b":
      for k in K:
        mr.emit_intermediate((k,j), {str(j)+","+str(i):value})

def reducer(key, list_of_values):
  # print key
  # print get_cell(list_of_values,key[0],0)
  # print get_cell(list_of_values,key[1],0)
  products = []
  for x in xrange(0,5):
    product = get_cell(list_of_values, key[0], x)
    if key[0] == key[1]:
      product = product * get_cell(list_of_values, key[1], x, True)
    else:
      product = product * get_cell(list_of_values, key[1], x)
    products.append(product)
  mr.emit((key[0],key[1],sum(products)))

def get_cell(list,i,j,second = False):
  value = 0
  hit_once = False
  for item in list:
    key = str(i) + "," +str(j)
    if key in item:
      if not second:
        value = item[key]
        break
      elif hit_once == 1:
        value = item[key]
        break
      else:
        hit_once = 1
  return value

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)