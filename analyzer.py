import operator
import re
import nltk.data
import io


def analyze(inputFile, outputFile, freqFile, PERCENT_SUMMARIZED, LENGTH_ADJUSTMENT_FACTOR, OPTIMAL_SENTENCE_LENGTH):
    #preparation
    input = open(inputFile)
    output = open(outputFile, 'w+')
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
    numSentences = float(len(tokenizedData))

    totalSentenceLength = 0
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
                totalSentenceLength = totalSentenceLength + wordCount
                sentenceTotal = sentenceTotal - (abs(wordCount - OPTIMAL_SENTENCE_LENGTH) / LENGTH_ADJUSTMENT_FACTOR)
            sentenceWeightBag[sentence] = sentenceTotal

    #find cutoff for sentence weight
    sortedSentenceWeightBag = sorted(sentenceWeightBag.items(), key=operator.itemgetter(1))
    cutoff = sortedSentenceWeightBag[-int(PERCENT_SUMMARIZED * numSentences / 100)][1]

    #show weight of each sentence
    for sentence in tokenizedData:
        print sentence + "\n"
        print sentenceWeightBag[sentence]
        print "\n---------\n"

    #print summarized sentences
    sentencesInOutput = 0
    for sentence in tokenizedData:
        if sentenceWeightBag[sentence] >= cutoff:
            sentencesInOutput = sentencesInOutput + 1
            output.write(sentence)
            output.write("\n----------\n")

    #show summarized status
    output.write("\n")
    output.write("\n")
    output.write("showing " + str(int(sentencesInOutput)) + " out of " + str(numSentences) + " sentences" + " (" + str(sentencesInOutput/numSentences * 100.00) + "%)\n")
    output.write("average sentence length is " + str(totalSentenceLength/numSentences) + " words")