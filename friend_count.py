#Kayla Hoffman
#COSI 143
#PA 3
#Problem 3
#Write a MapReduce algorithm to count the number of friends for each person.

import MapReduce
import sys

"""
Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    #record[0] is a person A
    #record[1] is their friend, person B
    #output is a personA and the friend personB
    mr.emit_intermediate(record[0], record[1])

# Implement the REDUCE function
def reducer(key, values):
    #key is person A
    #value is friend, person B
    count=0
    #sum total of tuples person A has
    for i in values:
        count +=1
    mr.emit((key, count))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
