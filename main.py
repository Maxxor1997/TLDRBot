from parser import parse
from analyzer import analyze
from aylienapiclient import textapi
import json

#config

client = textapi.Client("963c482b", "48dfe5e0273d1f852113c5479e09c72b")

url = "http://www.dailyprincetonian.com/article/2017/06/theres-trouble-a-bruin"

outputFile = "summarized.txt"

freqFile = "wordFreq.txt"


#settings

PERCENT_SUMMARIZED = 30

LENGTH_ADJUSTMENT_FACTOR = 10

OPTIMAL_SENTENCE_LENGTH = 20

SENTENCE_LOCATION_FACTOR = 2

WORD_IN_TITLE_FACTOR = 20


#run

extract = client.Extract({"url": url})

parse(extract.get('article').encode('ascii','xmlcharrefreplace'), "temp.txt")
parse(extract.get('title').encode('ascii','xmlcharrefreplace'), "titleTemp.txt")

analyze(url, "temp.txt", "titleTemp.txt", outputFile, freqFile, PERCENT_SUMMARIZED, LENGTH_ADJUSTMENT_FACTOR, OPTIMAL_SENTENCE_LENGTH, SENTENCE_LOCATION_FACTOR, WORD_IN_TITLE_FACTOR)

