class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while len(s)>i and len(t)>j:
            if s[i]==t[j]:
                i+=1
            j+=1

        return i==len(s)
        if i==len(s):
            return True
        else:
            return False
        
        
        