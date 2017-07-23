#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

inputFile = 'bnynews.txt'
outputFile = 'bnynewsParsed.txt'

input = open(inputFile, "r")
output = open(outputFile, "w")

inputString = input.read()

#remove quotation marks
inputString = inputString.replace("”", "\"")
inputString = inputString.replace("“", "\"")
inputString = inputString.replace("‘", "\'")
inputString = inputString.replace("’", "\'")
inputString = inputString.replace(". . . .", " ...")

# #remove periods that do not indicate sentence ends
# inputString = inputString.split(".”")
# inputString = inputString.replace("Mr.", "Mr")
# inputString = inputString.replace("Mrs.", "Mrs")
# inputString = inputString.replace("Ms.", "Ms")
# inputString = inputString.replace("Dr.", "Dr")
# inputString = inputString.replace("Jr.", "Jr")
# inputString = inputString.replace("p.m.", "pm")
# inputString = inputString.replace("a.m.", "am")
# inputString = re.sub('(?<=[A-Z])\.', '', inputString)
# inputString = re.sub(r"(\d)\.(\d)", r"\1,\2", inputString)

#remove empty spaces
output.write(' '.join(inputString.split()))


