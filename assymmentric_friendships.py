#Kayla Hoffman
#COSI 143
#PA 3
#Problem 4
#The relationship friend is often symmetric, meaning that if I am your friend, you are my friend.
#Implement a MapReduce algorithm to check whether this property holds.
#Generate a list of all non-symmetric friend relationships.
import MapReduce
import sys

"""
Assymetric Relationships in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    #record is in the form [personA, personB]
    #sort the two people as a tuple
    sort = tuple(sorted(record))
    #value is the record in reverse
    value = tuple((record[1], record[0]))
    mr.emit_intermediate(sort, value)


# Implement the REDUCE function
def reducer(key, recordList):
    #key: sorted record of persons A and B
    #value: tuple(B, A)
    if (len(recordList) == 1):
        mr.emit(recordList[0])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
