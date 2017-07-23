#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk.data
import io

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

fp = io.open("bnynewsParsed.txt", 'rU', encoding='utf-8')

data = fp.read()

tokenizedData = tokenizer.tokenize(data)

print type(tokenizedData)

print '\n-----\n'.join(tokenizedData)
#for token in tokenizedData:

    #print token

