import operator
import re

#settings

SENTENCES_IN_RESULT = 5
#between 1 and 10. the lower the number, the more shorter sentences are favored. 0 means lenghth not taken into account
LENGTH_ADJUSTMENT_FACTOR = 7
inputFile = "bnynewsParsed.txt"
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
#sortedWordBag = reversed(sorted(wordBag.items(), key=lambda item: item[1]))
#for tuple in sortedWordBag:
    #print tuple

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
            if LENGTH_ADJUSTMENT_FACTOR is not 0:
                sentenceTotal = sentenceTotal - (wordCount / LENGTH_ADJUSTMENT_FACTOR)
        sentenceWeightBag[sentence] = sentenceTotal

#find cutoff for sentence weight
sortedSentenceWeightBag = sorted(sentenceWeightBag.items(), key=operator.itemgetter(1))
cutoff = sortedSentenceWeightBag[-SENTENCES_IN_RESULT][1]

#print out sentences in order
print "Summarized Article: "
print ""
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
            if LENGTH_ADJUSTMENT_FACTOR is not 0:
                sentenceTotal = sentenceTotal - (wordCount / LENGTH_ADJUSTMENT_FACTOR)
        if (sentenceTotal >= cutoff):
            sentence = re.sub(r"\$(\d),(\d)", r"\1.\2", sentence)
            sentence = re.sub(r"\$(\d)(\d),(\d)", r"\1\2.\3", sentence)
            sentence = re.sub(r"\$(\d)(\d)(\d),(\d)", r"\1\2\3.\4", sentence)
            sentence = sentence.replace("Mr", "Mr.")
            sentence = sentence.replace("Mrs", "Mrs.")
            sentence = sentence.replace("Ms", "Ms.")
            sentence = sentence.replace("Dr", "Dr.")
            sentence = sentence.replace("Jr", "Jr.")
            print (sentence.lstrip() + ".")

#show summarized status
numSentences = float(len(re.split("\.|\?|!", inputString)))
print("")
print ("showing " + str(SENTENCES_IN_RESULT) + " out of " + str(numSentences) + " sentences" + " (" + str(SENTENCES_IN_RESULT / numSentences * 100) + "%)")