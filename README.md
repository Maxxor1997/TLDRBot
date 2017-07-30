NLTK Installation: http://www.nltk.org/install.html       
NLTK Data: http://www.nltk.org/data.html  
Article Scraper API: http://docs.aylien.com/  
Python version must be 2.7+

To run from main, set the following variables:  

<b>url</b> is the url of the article we want summarized  
<b>PERCENT_SUMMARIZED</b> is the percentage of sentences you want remaining after summary.       
<b>OPTIMAL_SENTENCE_LENGTH</b> is the length of the ideal summarized sentence. Studies have shown that the best readability occurs when the sentence is 15-20 words long.   
<b>LENGTH_ADJUSTMENT_FACTOR</b> is how much we want the lengths of the summarized sentences to match our optimal length. Lower means length is more important.  
<b>SENTENCE_LOCATION_FACTOR</b> is how much we want to favor sentences that occur earlier in the article. News articles often present the most important information first. Higher means location is more important.  
<b>WORD_IN_TITLE_FACTOR</b> is how much extra weight we give to words that appear in the title. Higher means we think title words are more relevant.  
<b>outputFile</b> determines where the summarized text is written to.

Debug:  
Word frequencies and sentence scores are shown in the console, along with the amount different factors affected the sentence score.

Known Errors:
NLTK tokenizer fails to recognize some acronyms like "F.B.I." and names like "Mr. Sessions" as use cases where the period does not indicate sentence ends.
