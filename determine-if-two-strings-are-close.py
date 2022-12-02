
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        h1,h2={},{}
        if len(word1)!=len(word2):
            return False
        elif set(word1)==set(word2):
            for i in range(len(word1)):
                h1[word1[i]]=h1.get(word1[i],0)+1
                h2[word2[i]]=h2.get(word2[i],0)+1
            val1=list(h1.values())
            val2=list(h2.values())
            for j in set(val1):
                if val1.count(j)!=val2.count(j):
                    return False
            return True
