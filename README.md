## Prerequisites
* [Python](https://www.python.org/download/releases/2.7/) - Python 2.7
* [NLTK](http://www.nltk.org/install.html) - Natural Language Processing Library
* [NLTK Data](http://www.nltk.org/data.html) - Subset of NLTK, used to split text into sentences

## Other Services Used
* [Aylien API](https://aylien.com/) - Natural Language Processing API, used to scrape article text and title from url.
* [Word Frequency Data](https://www.wordfrequency.info/free.asp) - Frequency of word occurrences in the English Language

## Settings in main.py
* **client** is the client object used to access Aylien API. My API key is hardcoded here, but feel free to use your own (keys are provided for free on the Aylien website).
* **url** is the url of the article to be summarized.
* **outputFile** determines where the summarized text is written to.
* **freqFile** is the text file that contains word frequency data. If you decide to use a different list from the one provided, you may have to edit how it's parsed in analyzer.py.

## Set Parameters in main.py
* **PERCENT_SUMMARIZED** is the percentage of sentences you want remaining after summary. For best results enter a number above 10.
* **OPTIMAL_SENTENCE_LENGTH** is the length of the ideal summarized sentence. Studies have shown that the best readability occurs when the sentence is 15-20 words long.
* **LENGTH_ADJUSTMENT_FACTOR** is how much you want the lengths of the summarized sentences to match the optimal length. Lower means length is more important.
* **SENTENCE_LOCATION_FACTOR** is how much you want to favor sentences that occur earlier in the article. News articles often present the most important information first. Higher means location is more important.
* **WORD_IN_TITLE_FACTOR** is how much you favor a word if it appears in the title. Higher value means you favor it more.

## Run
Inside IDE:
```
Run main.py
```
Command line:
```
cd TLDRBot
python main.py
```

## Debug:
* The frequencies of each word are shown in the console.
* Each sentence is printed in the console, along with its score and the contributors to that score
