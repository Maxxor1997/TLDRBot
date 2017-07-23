#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def parse(inputFile, outputFile):

    input = open(inputFile, "r")
    output = open(outputFile, "w")

    inputString = input.read()

    #replace non-ascii characters common in news articles
    inputString = inputString.replace("”", "\"")
    inputString = inputString.replace("“", "\"")
    inputString = inputString.replace("‘", "\'")
    inputString = inputString.replace("’", "\'")
    inputString = inputString.replace(". . . .", " ...")


    #remove empty spaces
    output.write(' '.join(inputString.split()))


