# Wordladder Search Problem
## Search, recursion and pattern matching example using Python

The wordladder exerceise is one of those rare problems that can be used to illustrate and explain multiple programming concepts. The problem statement is simple and its solution allows a writer to present various fundamental computer science techniques and structures in a concise manner. What is funny about this puzzel is that it was invented in 1878 by Lewis Carroll, the author of Alice in Wonderland, almost 70 years before the invention of the first computer. 

### Problem Statement

    Find the shortest path from a begin-word to an end-word such that we only change one single letter at each step.
    
In other words we need to find the smallest number of transformations such that at every transformation we change only one character. The words used to find the path are given as a list (which represent the dictionary space of available words).

### Example

Assuming these 3 letter words represent our dictionary  

    dictList = ["lot","hat", "hot", "log","dog","pot","dot"]

then it takes a minimum of 5 steps to convert the word hit -> cog 
 
    hit -> hot -> dot -> dog -> cog

Typically, the solution for this problem utilizes graphs and graph algorithms (https://leetcode.com/problems/word-ladder/). However, in our post we utilize a different approach that is both easier to understand and more elegant to program.

Before we start lets list a few programming concepts which we shall be applying throughout our discussion.

- Recursion
- Backtracking
- Tree search
- Pattern Matching


