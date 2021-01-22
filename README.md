# Wordladder Search Problem
## Search, recursion and pattern matching example using Python

The wordladder exerceise is one of those rare problems that can be used to illustrate programming concepts in a concise manner. The problem is simple, yet it allows a programmer to elaborate a solution at various levels of complexity. What is funny about this puzzel is that it was invented in 1878 by Lewis Carroll, the author of Alice in Wonderland, almost 70 years before the invention of the first computer. 

### Problem Statement

    Find the shortest path from a begin-word to an end-word such that we only change one single letter at each step.
    
In other words we need to find the smallest number of transformations such that at every transformation we only change one character. The words used to find the path are given as a list (which represent the available vocabulary or dictionary).

### Example

Assuming the following list of 3 letter words being our dictionary  

    dictList = ["lot", "hit", "hot", "log","dog", "dot"]

then it takes a minimum of 4 steps to convert the word hit -> fog 
 
    hit -> hot -> dot -> dog -> fog

Typically, the solution for this problem utilizes graphs and graph algorithms (https://leetcode.com/problems/word-ladder/). However, in our post we utilize a different approach that is both easier to understand and more elegant to present in a tutorial article.

Before we start lets list a few programming concepts which we shall be applying throughout our discussion.

- Recursion
- Backtracking
- Tree search
- Pattern Matching
- Optimization

### Matching & Comparing

The code snippet below is our first attempt to finding the basic operations required for the task

    # wordladder.py
    class WordLadder:
        def doMatch(self, wordl, wordr):
            pattern = []
            for (cl,cr) in zip(wordl,wordr):
                if cl == cr:
                    pattern.append('*')
                else:
                    pattern.append (cr)
            return ("".join(pattern))

        def compare(self, pattern):
            return (len(pattern) - pattern.count('*') == 1)

We can use the above class as follows:

>> 
