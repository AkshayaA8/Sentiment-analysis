#!/usr/bin/env python

from __future__ import division
from operator import itemgetter
import sys
import csv

# Main reducer function 
def main():
	sAvg = 0.0
	sNum = 0
	aAvg = 0.0
	aNum = 0
	for line in sys.stdin:
		line = line.strip()       
		row = line.split('\t')
		key = row[1]
		avg = row[2]

		try:
			avg = float(avg)
		except:
			continue
        
		if key == 'samsung':
			sAvg += avg
			sNum += 1

		if key == 'apple':
			aAvg += avg
			aNum += 1

	print ('Overall average score of the products\n')
	print '%s\t%.4f' % ('samsung',sAvg/sNum)
	print '%s\t%.4f' % ('apple',aAvg/aNum)	

if __name__ == '__main__':
    main()
