class Solution:
    def oddString(self, words: List[str]) -> str:
        di={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        n=len(words[0])
        res={}
        for i in words:
            l=[]
            for j in range(n-1):
                l.append(di[i[j+1]]-di[i[j]])
            res[i]=l
        for key,value in res.items():
            if list(res.values()).count(value)==1 and words.count(key)==1:
                return key
