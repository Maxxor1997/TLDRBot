NLTK Installation: http://www.nltk.org/install.html       
NLTK Data: http://www.nltk.org/data.html   
Python version must be 2.7+

To run from main, set the following variables:  
-inputFile is the text file to be summarized (non-ASCII characters may break code)  
-PERCENT_SUMMARIZED is the percentage of sentences you want remaining after summary. For best results enter a number above 10.       
-OPTIMAL_SENTENCE_LENGTH is the length of the ideal summarized sentence. Studies have shown that the best readability occurs when the sentence is 15-20 words long.
-LENGTH_ADJUSTMENT_FACTOR is how much we want the lengths of the summarized sentences to match our optimal length. Lower means length is more important.  
-SENTENCE_LOCATION_FACTOR is how much we want to favor sentences that occur earlier in the article. News articles often present the most important information first. Higher means location is more important.
-outputFile determines where the summarized text is written to.

Debug:  
Word frequencies and sentence scores are shown in the console.
