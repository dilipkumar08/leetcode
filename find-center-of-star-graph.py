class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        map={}
        l=len(edges)
        for i in edges:
            for j in i:
                map[j]=map.get(j,0)+1
        
        for key,value in map.items():
            if value==l:
                return key
