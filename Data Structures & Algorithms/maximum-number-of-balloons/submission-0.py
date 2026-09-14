class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap={}
        for i in range(len(text)):
            if text[i] in hashmap:
                hashmap[text[i]]+=1
            else:
                hashmap[text[i]]=1

        res=float("inf")

        for i in "balloon":
            if i in hashmap:
                count=hashmap[i]
            else:
                count=0
            if i=='l' or i=='o':
                count=count//2
            res=min(res,count) 
        return res

        