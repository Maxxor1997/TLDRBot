import operator
import re

#settings
SENTENCES_IN_RESULT = 7
LENGTH_ADJUSTMENT_FACTOR = 3 #between 1 and 10. the lower the number, the more shorter sentences are favored
inputFile = "princetonParsed.txt"
freqFile = "wordFreq.txt"

#preparation
input = open(inputFile)
wordFreq = open(freqFile)
inputString = input.read()

freqBag = {}
#populate dictionary with information from wordFreq.txt
for line in wordFreq:
    word = str.lower(re.sub("[^a-zA-Z]", "", line.split()[0]))
    freq = float(line.split()[-1])
    freqBag[word] = freq

print freqBag

#populate word frequency list for article
wordBag = {}
for word in inputString.split():
    word = re.sub("[^a-zA-Z]", "", word)
    word = str.lower(word)
    if word:
        if not word in wordBag:
            wordBag[word] = 1.00
        else:
            wordBag[word] = wordBag[word] + 1.00

#for display
sortedWordBag = reversed(sorted(wordBag.items(), key=lambda item: item[1]))
for tuple in sortedWordBag:
    print tuple

sentenceWeightBag = {}
#add values to sentence weight bag
for sentence in re.split("\.|\?|!", inputString):
    if len(sentence) > 0.00:
        sentenceTotal = 0.00
        wordCount = 0.00
        for word in sentence.split():
            word = str.lower(word)
            #print wordCount
            wordCount = wordCount + 1
            word = re.sub("[^a-zA-Z]", "", word)
            if word in wordBag:
                if word in freqBag:
                    sentenceTotal = sentenceTotal + (wordBag[word] / freqBag[word])
                else:
                    sentenceTotal = sentenceTotal + (wordBag[word] / 10.00)
        if not wordCount is 0.00:
            #print ("sentence total: " + str(sentenceTotal))
            #print ("wordCount: " + str(wordCount))
            #print sentenceTotal
            #print wordCount
            #print sentenceTotal
            #print wordCount
            sentenceTotal = sentenceTotal - (wordCount / LENGTH_ADJUSTMENT_FACTOR)
            #print sentenceTotal
        sentenceWeightBag[sentence] = sentenceTotal

#find cutoff for sentence weight
sortedSentenceWeightBag = sorted(sentenceWeightBag.items(), key=operator.itemgetter(1))
cutoff = sortedSentenceWeightBag[-SENTENCES_IN_RESULT][1]

#print out sentences in order
for sentence in re.split("\.|\?|!", inputString):
    if len(sentence) > 0.00:
        sentenceTotal = 0.00
        wordCount = 0.00
        for word in sentence.split():
            word = str.lower(word)
            wordCount = wordCount + 1
            word = re.sub("[^a-zA-Z]", "", word)
            if word in wordBag:
                if word in freqBag:
                    sentenceTotal = sentenceTotal + (wordBag[word] / freqBag[word])
                else:
                    sentenceTotal = sentenceTotal + (wordBag[word] / 10.00)
        if not wordCount is 0.00:
            sentenceTotal = sentenceTotal - (wordCount / LENGTH_ADJUSTMENT_FACTOR)
        if (sentenceTotal >= cutoff):
            print ("sentence: " + sentence + ".")

#show summarized status
numSentences = float(len(re.split("\.|\?|!", inputString)))
print("")
print ("showing " + str(SENTENCES_IN_RESULT) + " out of " + str(numSentences) + " sentences" + " (" + str(SENTENCES_IN_RESULT / numSentences * 100) + "%)")