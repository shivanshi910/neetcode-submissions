class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap={}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]+=1
            else:
                hashmap[s[i]]=1

        res=float("-inf")
        for odd in hashmap.values():
            if odd % 2==0:
                continue
            for even in hashmap.values():
                if even%2==1:
                    continue
                res= max(res,odd-even)
        return res
        