#Kayla Hoffman
#COSI 143
#PA 3
#Problem 5
#Assume you have two 5 x 5 matrices A and B in a sparse matrix format,
#where each record is of the form i, j, value. Design a MapReduce algorithm
#to compute the matrix multiplication A x B.
import MapReduce
import sys

"""
Matrix Multiply in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
     #input: [matrix, i, j, value], i is the row, j is the column
     matrix = record[0]
     i = record[1]
     j = record[2]
     value = record[3]
     if (matrix == "a"):
         for k in range(5):
             mr.emit_intermediate((i, k), (matrix, j, value))
     else:
         for l in range(5):
             mr.emit_intermediate((l, j), (matrix, i, value))

# Implement the REDUCE function
def reducer(key, values):
    #key: row and column pair
    #values: list of matrix, i or j, and cell value
    sum = 0
    #what has already been added to the output
    dict= []
    for t1 in values:
        for t2 in values:
            if ((t1[0] != t2[0]) & (t1[1] == t2[1])):
                output = tuple((t1[1], t2[1]))
                #add only if new, otherwise value of cell wrong
                if (output not in dict):
                    dict.append(output)
                    sum += (t1[2] * t2[2])
    mr.emit((key[0], key[1], sum))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
