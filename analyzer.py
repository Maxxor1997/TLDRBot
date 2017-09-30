import operator
import re
import nltk.data
import io


def analyze(url, inputFile, titleFile, outputFile, freqFile, PERCENT_SUMMARIZED, LENGTH_ADJUSTMENT_FACTOR, OPTIMAL_SENTENCE_LENGTH, SENTENCE_LOCATION_FACTOR, WORD_IN_TITLE_FACTOR):
    #preparation
    input = open(inputFile)
    inputString = input.read()
    title = open(titleFile).read()
    print(title)
    output = open(outputFile, 'w+')
    output.write("url: " + url + '\n')
    output.write("\n---------\n")
    wordFreq = open(freqFile)

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
                wordBag[word] = 1
            else:
                wordBag[word] = wordBag[word] + 1

    #populate word list for title
    titleBag = {}
    for word in title.split():
        word = re.sub("[^a-zA-Z]", "", word)
        word = str.lower(word)
        if word:
            if not word in titleBag:
                titleBag[word] = 1
            else:
                titleBag[word] = titleBag[word] + 1

    #for display
    sortedWordBag = reversed(sorted(wordBag.items(), key=lambda item: item[1]))
    for tuple in sortedWordBag:
        print tuple

    # segment into sentences
    extra_abbreviations = ["F.B.I", "Mr. Sessions"]
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    tokenizer._params.abbrev_types.update(extra_abbreviations)
    tokenizedData = tokenizer.tokenize(inputString)
    numSentences = float(len(tokenizedData))

    totalSentenceLength = 0
    sentenceWeightBag = {}
    #add values to sentence weight bag
    nthSentence = 0
    for sentence in tokenizedData:
        print sentence + "\n"
        nthSentence = nthSentence + 1
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
                    if word in titleBag:
                        if word in freqBag:
                            sentenceTotal = sentenceTotal + (WORD_IN_TITLE_FACTOR/freqBag[word])
                            print (word + " in title added " + str(WORD_IN_TITLE_FACTOR/freqBag[word]) + " points")
                        else:
                            sentenceTotal = sentenceTotal + (WORD_IN_TITLE_FACTOR / 10.00)
                            print (word + " in title added " + str(WORD_IN_TITLE_FACTOR / 10.00) + " points")
            if not LENGTH_ADJUSTMENT_FACTOR is 0 and not wordCount is 0.00:
                sentenceTotal = sentenceTotal - (abs(wordCount - OPTIMAL_SENTENCE_LENGTH) / LENGTH_ADJUSTMENT_FACTOR)
                print('')
                print("sentence length handicap is " + str(abs(wordCount - OPTIMAL_SENTENCE_LENGTH) / LENGTH_ADJUSTMENT_FACTOR))
            elif not wordCount is 0.00:
                totalSentenceLength = totalSentenceLength + wordCount
            sentenceTotal = sentenceTotal - (nthSentence / numSentences * SENTENCE_LOCATION_FACTOR)
            print('')
            print ("sentence location handicap is " + str((nthSentence / numSentences * SENTENCE_LOCATION_FACTOR)))
            sentenceWeightBag[sentence] = sentenceTotal
        print ("\n" + str(sentenceTotal))
        print "\n---------\n"
    #find cutoff for sentence weight
    sortedSentenceWeightBag = sorted(sentenceWeightBag.items(), key=operator.itemgetter(1))
    cutoff = sortedSentenceWeightBag[-int(PERCENT_SUMMARIZED * numSentences / 100)][1]

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
    #output.write("average sentence length is " + str(totalSentenceLength/numSentences) + " words")