class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        
        
        if len(s)!=len(t):
            return False
        for s1 in s:
            if s1 not in dict_s:
                dict_s[s1]=1
            else:
                dict_s[s1]+=1
                
        for t1 in t:
            if t1 not in dict_s:
                return False
            else:
                dict_s[t1]-=1
        for val in dict_s.values():
            if val!=0:
                return False
        return True
  