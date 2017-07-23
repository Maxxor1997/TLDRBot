import operator
import re
import nltk.data
import io


#settings

SENTENCES_IN_RESULT =7
#between 1 and 10. the lower the number, the more shorter sentences are favored. 0 means lenghth not taken into account
LENGTH_ADJUSTMENT_FACTOR = 5
inputFile = "nytimesParsed.txt"
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
sortedWordBag = reversed(sorted(wordBag.items(), key=lambda item: item[1]))
for tuple in sortedWordBag:
    print tuple

# segment into sentences
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
tokenizedData = tokenizer.tokenize(inputString)

sentenceWeightBag = {}
#add values to sentence weight bag
for sentence in tokenizedData:
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
        sentenceWeightBag[sentence] = sentenceTotal

#find cutoff for sentence weight
sortedSentenceWeightBag = sorted(sentenceWeightBag.items(), key=operator.itemgetter(1))
cutoff = sortedSentenceWeightBag[-SENTENCES_IN_RESULT][1]

#show weight of each sentence
for sentence in tokenizedData:
    print sentence + "\n"
    print sentenceWeightBag[sentence]
    print "\n---------\n"

#print summarized sentences
for sentence in tokenizedData:
    if sentenceWeightBag[sentence] >= cutoff:
        print "\n----------\n"
        print sentence

#show summarized status
numSentences = float(len(tokenizedData))
print("")
print ("showing " + str(SENTENCES_IN_RESULT) + " out of " + str(numSentences) + " sentences" + " (" + str(SENTENCES_IN_RESULT / numSentences * 100) + "%)")