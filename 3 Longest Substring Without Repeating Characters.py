class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_string_start=0
        longest_len=0
        cur_len=0
        dict_={}
        for i,j in enumerate(s):
            if j in dict_ and dict_[j]>=cur_string_start:
                cur_string_start=dict_[j]+1
                cur_len=i-dict_[j]
                dict_[j]=i
            else:
                dict_[j]=i
                cur_len+=1
                if longest_len<cur_len:
                    longest_len=cur_len
        return longest_len
