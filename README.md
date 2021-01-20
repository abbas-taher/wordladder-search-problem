# Wordladder Search Problem
## Search, recursion and pattern matching example using Python

The wordladder exerceise is one of those rare programming problems that can be used to illustrate a number of programming concepts with clarify and in a concise mannner.
The problem can be solved in an elegant and concise manner in order to - in this case tree search.

The problem is quite simple.

    Find the shortest path from a starting word to an end word such that we only change one single letter at each step.
    
In other words we need to find the smallest number of transformations such that at every transformation we change only one character. The words used to find the path are given as a list (which represent the dictionary space of available words).

Example:

Assuming all these 3 letter words are there in the dictionary provided, it takes minimum 4 transitions to convert word from SAIL to RUIN, i.e.
SAIL -> MAIL -> MAIN -> RAIN -> RUIN

In a typical solution given often utilize graphs and graph algorithms to solve this problem. However, the solution given here takes a different approach which is easier to understand and more elegant.
