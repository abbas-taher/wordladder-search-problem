# Wordladder Search Problem
## Search, recursion and pattern matching example using Python

The wordladder exerceise is one of those rare problems that can be used to illustrate programming concepts in a concise manner. The problem is simple, yet it allows a programmer to elaborate a solution at various levels of complexity. What is funny about this puzzel is that it was invented in 1878 by Lewis Carroll, the author of Alice in Wonderland, almost 70 years before the invention of the first computer. 

### Problem Statement

    Find the shortest path from a begin-word to an end-word such that we only change one single letter at each step.
    
In other words we need to find the smallest number of transformations such that at every transformation we only change one character. The words used to find the path are given as a list (which represent the available vocabulary or dictionary).

### Example

Assume a dictionary consisting of the following list of 3 letter words:   

    dictList = ['hot','log','dog','dot','lot']

then it takes a minimum of 4 steps to convert the word hit -> fog 
 
    hit -> hot -> dot -> dog -> fog

Typically, the solution for this problem utilizes graphs and graph algorithms (https://leetcode.com/problems/word-ladder/). However, in our post we utilize a different approach that is both easier to understand and more elegant to present in a tutorial article.

Before we start lets list a few programming concepts which we shall be applying during our discussion.
- Pattern Matching
- Recursion
- Backtracking
- Tree Search
- Tree Pruning

### v0. Matching & Comparing

The code snippet below is our first attempt to finding the basic functions (operations) needed for the task.

    # wordladder_v0.py
    class WordLadder:
        def doMatch(self, wordl, wordr):
            pattern = []
            for (cl,cr) in zip(wordl, wordr):
                if cl == cr:
                    pattern.append('*')
                else:
                    pattern.append (cr)
            return ("".join(pattern))

        def counts(self, pattern):
            return (len(pattern) - pattern.count('*') == 1)
    
    dictList = ['hot','log','dog','dot','lot']
    
To test the two function we can just import wordladder.py from within the Python shell then call the two methods.

    $ python 
    >>> import wordladder_v0.py
    >>> start, end  = 'hit', 'fog' 
    >>> wl = WordLadder()
    >>> pattern1 = wl.doMatch('hit','hot')
    >>> print (pattern1, wl.compare(pattern1))
      *o* True

    >>> pattern2 = wl.doMatch('dot','fog')
    >>> print (pattern2, wl.counts(pattern2))
      f*g False

    >>> pattern3 = wl.doMatch('hit','hit')
    >>> print (pattern3, wl.counts(pattern3))
      *** False

The pattern matching method **doMatch** takes two parameters: left and rigth words. It returns all matching characters as '\*' and the remaining ones from the word to the right - i.e. the word we are trying to transform to). The **counts** method simply returns *True* when only one character does not match (is not '\*') in a given pattern. It does so by counting the number of '\*' in the given pattern.

### v1. Tree Search: Simple Recursion

Using the above two functions, we can now write our 1st wordladder algorithm which is a simple function that takes a begin-word and a list of words and recursively searches for a matching word - i.e a word that is one character different from the begin-word. As show in the code below, the algorithm does not do any special optimization. It just returns the first path it finds.     

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
            for word in wordList:
                pattern = self.doMatch(begin, word)
                if self.counts(pattern):
                    remain = wordList[:]                  # make a local copy
                    remain.remove(word)                   # pop the word 
                    pathlst = self.ladder(word, remain)   # pass remaining to the next recursive call
                    if pathlst:
                        return ([begin] + pathlst)
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


To execute the code we can just run the wordladder_v1.py program using a call to Python via the command line:

  $ python wordladder_v1.py

This will produce two paths, one for dictList and other for wordList:

     ['hit', 'hot', 'dot', 'dog', 'fog']           # using dictList
     ['hit', 'hot', 'lot', 'dot', 'dog', 'fog']    # using wordList
     
So why is one path longer than the other, even though both lists contain the same set of words? If you look curefully you will see that both lists are ordered differently, in which case the ladder method traverses the search tree along a different path depending on what it sees first at each recursion; thus, returning the first path it finds. 

To fully understand this, we need to look at the tree we are trying to search based on the recursion order. For example, for the dictList, the tree below represents the different branches that actually produces a final path. There are other branches that do not, in which case they are not listed here. As you can see the first path is the one printed above and it happens to be the shortest path as well. 

    hit -> hot -> dot -> dog -> fog
    hit -> hot -> dot -> lot -> log -> dog -> fog
    hit -> hot -> dot -> log -> dog -> fog
    hit -> hot -> lot -> log -> fog 
    hit -> hot -> lot -> log -> dog -> fog 
    hit -> hot -> lot -> dot -> dog -> fog

When we shuffled the words and use wordList instead, the path found becomes longer. Here, it happens to be the last branch in the above list.

#### Backtracking

It is important to note that the recursive algorithm uses backtracking to generate the full path. This is illustrated by the lines below. Here, if the *pathlist* returned by the recursive call to ladder, is not empty it is concatenated to the begin-word and then returned to the parent call. As a result the full path list gets built and then propagated back to the first ladder called by the *find* method.  

    if self.counts(pattern):
        remain = wordList[:]
        remain.remove(word)   
        pathlst = self.ladder(word, remain)
        if pathlst:
            return ([begin] + pathlst)        # backtracking happens here
            
            
### v2. Tree Search: Shortest Path

Of course, the ladder method above which returns the first path found while traversing the search tree is not good enough because we are interested in finding the shortest path amongst all possible paths. The skeleton of the ladder code below is quite similar to the one shown above, but with an additional tests for the shortest path. Basically, the method checkes if any of the sub paths (tree branches) retuned by its recursive calls is shorter than the one it already has. Onces it checks all subpaths it returns it to the caller or else returns an empty path (because all the sub-branches) could not terminate properly.
    
    # wordladder_v2.py
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
                    elif pathlst != [] and (len(pathlst) <= len(shortest_path)):   # found a new path and it is shorter 
                        shortest_path = pathlst                                    # reassign as shortest path
            if shortest_path != []:
                return ([begin] + shortest_path)                                   # return shortest path to the parent 
            else:                                                                  # which called this ladder method
                return ([])                                                        # return [] bcs loop could'nt find any path

### v3. Tree Pruning
 
 that reduces the size of decision trees by removing sections of the tree that are non-critical and redundant to classify instances. 
 
### Concluding Remarks

We can clearly see now after this deep dive that search program may look deceivingly simple. The code is both compact and efficient. Understanding how things actually work requires a deeper knowledge of recursive programming, tree search and pruning as well as pattern matching.
