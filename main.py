from parser import parse
from analyzer import analyze

#settings

SENTENCES_IN_RESULT =7

#between 1 and 10. the lower the number, the more shorter sentences are favored. 0 means length not taken into account
LENGTH_ADJUSTMENT_FACTOR = 5

inputFile = "nytimes.txt"

outputFile = "summarized.txt"

freqFile = "wordFreq.txt"

parse(inputFile, "temp.txt")
analyze("temp.txt", outputFile, freqFile, SENTENCES_IN_RESULT, LENGTH_ADJUSTMENT_FACTOR)

