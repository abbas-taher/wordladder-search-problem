# Wordladder Search Problem
## Search, recursion and pattern matching example using Python

The wordladder exerceise is one of those rare problems that can be used to illustrate programming concepts in a concise manner. The problem is simple, yet it allows a programmer to elaborate a solution at various levels of complexity. What is funny about this puzzel is that it was invented in 1878 by Lewis Carroll, the author of Alice in Wonderland, almost 70 years before the invention of the first computer. 

### Problem Statement

    Find the shortest path from a begin-word to an end-word such that we only change one single letter at each step.
    
In other words we need to find the smallest number of transformations such that at every transformation we only change one character. The words used to find the path are given as a list (which represent the available vocabulary or dictionary).

### Example

Assume a dictionary consisting of the following list of 3 letter words:   

    dictList = ["lot", "hit", "hot", "log","dog", "dot"]

then it takes a minimum of 4 steps to convert the word hit -> fog 
 
    hit -> hot -> dot -> dog -> fog

Typically, the solution for this problem utilizes graphs and graph algorithms (https://leetcode.com/problems/word-ladder/). However, in our post we utilize a different approach that is both easier to understand and more elegant to present in a tutorial article.

Before we start lets list a few programming concepts which we shall be applying during our discussion.
- Pattern Matching
- Recursion
- Backtracking
- Tree search
- Optimization

### v0. Matching & Comparing

The code snippet below is our first attempt to finding the basic functions (operations) needed for the task.

    # wordladder_v0.py
    class WordLadder:
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
    
    dictList = ["lot", "hit", "hot", "log","dog", "dot"]
    
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

The pattern matching method **doMatch** returns all matching characters as '\*' and the remaining ones from the right word - i.e. the word we are trying to transform to). The **counts** method simply returns *True* when only one character does not match. It does so by counting the number of '\*' in the given pattern.

### v1. Simple Recursion

So far we have not done any search, so lets add this code to our class which not looks as follows:


