# wordladder_v1.py
class WordLadder:
    def __init__(self, start, end, wordList):
        self.start = start
        self.end = end
        self.wordList = wordList
        
    def find(self):
        pathlst = self.ladder(self.start, self.wordList)
        return (pathlst + [self.end])
        
    def ladder(self, begin, wordList):
        pattern = self.doMatch(begin, self.end)
        if self.counts(pattern):
            return ([begin])
        
        shortest_path = []
        for word in wordList:
            pattern = self.doMatch(begin, word)
            if self.counts(pattern):
                remain = wordList[:]
                remain.remove(word)
                pathlst = self.ladder(word, remain)
                if shortest_path == []:
                    shortest_path = pathlst 
                elif pathlst != [] and (len(pathlst) <= len(shortest_path)):
                    shortest_path = pathlst
        if shortest_path != []:
            return ([begin] + shortest_path)
        else:
            return ([])
    
    
    def doMatch(self, wordl, wordr):
        pattern = []
        for (cl,cr) in zip(wordl,wordr):
            if cl == cr:
                pattern.append('*')
            else:
                pattern.append (cr)
        return ("".join(pattern))
    
    def counts(self, pattern):
        return (len(pattern) - pattern.count('*') == 1)

dictList = ['hot','log','dog','dot','lot']

start, end = 'hit','fog'
wl = WordLadder(start,end, dictList)
print (wl.find())                       # -> ['hit', 'hot', 'dot', 'dog', 'fog']

wordList = ['lot','hot','dog','dot','log']  
wl = WordLadder(start,end, wordList)
print (wl.find())                       # -> ['hit', 'hot', 'lot', 'dot', 'dog', 'fog']

