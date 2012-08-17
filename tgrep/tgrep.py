#!/usr/bin/env python
"""
Description:
    Simple script to grep through various log files in basic syslog format to retrieve timeframes.
    The search mechanism is basic, but syslog files aren't big.

Author:
    Robb O'Driscoll.  <https://twitter.com/oh_rodr>
    Twitter Security

Copyright 2012 Twitter Inc.
"""

version = "0.01"

import os, sys
import stat
from datetime import date,datetime
import re
from optparse import OptionParser
import gzip
import time

def getPassed():
    usage = "usage: %prog [options] filename"

    parser = OptionParser(usage=usage)
    parser.add_option('-z','--zip',
                      action='store_true', dest='zip',help='gzip file?')
    parser.add_option('-x','--plaintext',
                      action='store_false', dest='zip',help='plaintext file?')
    parser.add_option('-e','--end',
                      dest='end',help='end time to search: %b %d %H:%M:%S Feb 28 00:00:00 format')
    parser.add_option('-s','--start',
                      dest='start',help='start time to search: %b %d %H:%M:%S Feb 28 00:00:00 format')

    parser.add_option('-f','--full',
                      action='store_true',dest='full',help='complete search?')

    parser.add_option('-r','--regex',
                      dest='regex',help='regex to search')

    (options,args) = parser.parse_args()
    return (options,args)

def parseline(line):
    """ Does basic parsing against RFC syslog lines
        Input a line return tuple(date,string)
    """
    if line == '':
        print("EOF reached")
        exit(1)
    if line[-1] == '\n':
        line = line.rstrip('\n')

    words = line.split(' ')
    if len(words) >3:
        linedate = ' '.join(words[0:3])
        line = ' '.join(words[5:])
    else:
        linedate = ''
    return (linedate,line)

def check_answer(l,options):
    """ input a given line, and check if the string is worth while.
    """
    lineTime =  time.strptime(l[0],'%b %d %H:%M:%S')
    startTime = time.strptime(options.start,'%b %d %H:%M:%S')
    if options.end:
        endTime =   time.strptime(options.end,'%b %d %H:%M:%S')
    else:
        endTime =   time.strptime(options.start,'%b %d %H:%M:%S')
    if startTime <= lineTime:
        if lineTime <= endTime: 
            if options.regex:
                # if the user supplied regex
                # only return the lines that match
                ur = re.compile(options.regex)
                if re.search(ur,l[1]):
                    print l
                    return l
                else:
                    return None
            # if there's no regex return the line
            print l
            return l
    if options.full == True: 
        # if we want the full file scan
        # continue
        return None
    if lineTime > endTime:  return('!')
    
def getlines(fh,options,args):
    """ gets the lines we care about. """
    lines = []
    if options.zip == True:
        with gzip.GzipFile(args[0],'r') as f:
            while 1:
                filelines = f.readlines(100000)
                if not filelines:
                    break
                for line in filelines:
                    if check_answer(parseline(line),options) == '!': break
                    if check_answer(parseline(line),options):
                        lines.append(check_answer(parseline(line),options))
    else:
        with open(args[0],'r') as f:
            while 1:
                filelines = f.readlines(75000)
                if not filelines:
                    break
                for line in filelines:
                    if check_answer(parseline(line),options) == '!': break
                    if check_answer(parseline(line),options):
                        lines.append(check_answer(parseline(line),options))
    return lines

def run():
    (options,args) = getPassed()
    lines = []
    try:
        args[0] 
    except:
        print "give me a filename"
        exit(1)
    if options.zip == True:
        with gzip.GzipFile(args[0],'r') as f:
            lines = getlines(f,options,args)
    else:
        with open(args[0],'r') as f:
            lines = getlines(f,options,args)
    return lines
        
if __name__ == '__main__':
    print run()
