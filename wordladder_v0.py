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

dictList = ['hot','log','dog','dot','lot']