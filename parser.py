#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def parse(inputString, outputFile):

    output = open(outputFile, "w")

    #replace common non-ascii characters with ascii ones
    inputString = inputString.replace("&#8220;", "\"")
    inputString = inputString.replace("&#8221;", "\"")
    inputString = inputString.replace("&#8217;", "\'")
    inputString = inputString.replace("&#8216;", "\'")
    inputString = inputString.replace("&#8212;", "-")
    inputString = inputString.replace("&#160;", " ")
    inputString = inputString.replace("‘", "\'")
    inputString = inputString.replace("’", "\'")
    inputString = inputString.replace("é", "e")
    inputString = inputString.replace(". . . .", " ...")

    #to fix some commonly encountered issues with the nltk sentence segmenter
    #inputString = inputString.replace("F.B.I.", "F.B.I")
    #inputString = inputString.replace("Mr. Sessions", "Mr. Shoe")

    #remove empty spaces
    output.write(' '.join(inputString.split()))


