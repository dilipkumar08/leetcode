class Solution(object):
    def checkIfPangram(self, s):
        if len(set(s))==26:
            return True
        else:
            return False
        
