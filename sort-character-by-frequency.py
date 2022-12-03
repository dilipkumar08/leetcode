class Solution:
    def frequencySort(self, s: str) -> str:
        h1={} #dictionary one for character count in char-count format
        h2={} #dictionary two for count of characters with same count in count-list of char format
        temp="" #to store the resultant string
        
        #finding character count
        for i in s:
            h1[i]=h1.get(i,0)+1
        
        #finding the count of characters with same count
        for j in h1:
            if h1[j] not in h2:
                h2[h1[j]]=[j]
            else:
                h2[h1[j]].append(j)
        
        #creating the resultant string with h2
        for k in sorted(h2,reverse=True):
            for l in h2[k]:
                temp+=k*l
        return temp
