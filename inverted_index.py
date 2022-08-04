#Kayla Hoffman
#COSI 143
#PA 3
#Problem 1
#Description: Given a set of documents, an inverted index is a dictionary where each word
#is associated with a list of the document identifiers in which that word appears.
import MapReduce
import sys

"""
Inverted Index Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    #record: the document name and then the words within it
    #split words by spaces
    valueArray = record[1].split()
    #emit word and the name of the doc
    for word in valueArray:
        mr.emit_intermediate(word, record[0])

# Implement the REDUCE function
def reducer(key, values):
    #key: the actual word
    #values: the documents where the word appears
    #create list to add all documents where word appears
    docList = []
    #for each appearance
    for i in values:
        #add doc if not already in the list
        if i not in docList:
            docList.append(i)
    #emit key word and list of docs
    mr.emit((key, docList))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
