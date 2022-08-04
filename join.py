#Kayla Hoffman
#COSI 143
#PA 3
#Problem 2
#Implement a relational join as a MapReduce query

import MapReduce
import sys

"""
JOIN in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    #record is the whole tuple icluding the table of origin as [0]
    #record[1] is the order_id
    mr.emit_intermediate(record[1], record)

# Implement the REDUCE function
def reducer(key, values):
    #key: order_id
    #values: tuples with the same order_id
    join_result=[]
    for t1 in values:
        for t2 in values:
            if t1[0] != t2[0]:
                output = (t1, t2)
                #if output has not appeared before
                if output not in join_result:
                    join_result.append(output)
    mr.emit(join_result)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
