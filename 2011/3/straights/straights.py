#!python
# Dire Straights http://code.google.com/codejam/contest/dashboard?c=1158485#s=p1
from __future__ import division
import math
from collections import deque
import sys
from optparse import OptionParser
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if args:
    if args[0] == "-":
        f = sys.stdin
    else:
        f = open(args[0])
elif not sys.stdin.isatty():
    f = sys.stdin
else:
    parser.error("Need input from file or stdin")

T = int(f.readline())
                      
for i in range(1,T+1):
    line = [int(x) for x in f.readline().split()]
    N = line[0]
    cards = sorted(line[1:])
    assert len(cards) == N
    #print cards
    straights = []
    for x in cards:
        for straight in reversed(straights):
            if straight[-1] == x-1:
                straight.append(x)
                break
        else:
            straight = [x]
            straights.append(straight)
        #print straights
        lengths = [len(straight) for straight in straights]
        #print lengths
        assert lengths == sorted(lengths,reverse=True)
    answer = 0
    if straights:
        answer = min(len(straight) for straight in straights)
    print "Case #%d: %s" % (i,answer)
        
        