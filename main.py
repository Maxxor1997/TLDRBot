from parser import parse
from analyzer import analyze

#settings

PERCENT_SUMMARIZED = 15

LENGTH_ADJUSTMENT_FACTOR = 0

OPTIMAL_SENTENCE_LENGTH = 20

SENTENCE_LOCATION_FACTOR = 10

inputFile = "Sample Text Files/nytimes1.txt"

outputFile = "summarized.txt"

freqFile = "wordFreq.txt"

parse(inputFile, "temp.txt")
analyze("temp.txt", outputFile, freqFile, PERCENT_SUMMARIZED, LENGTH_ADJUSTMENT_FACTOR, OPTIMAL_SENTENCE_LENGTH, SENTENCE_LOCATION_FACTOR)

