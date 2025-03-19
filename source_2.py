# Used 2588ms of runtime. By the way this works for all inputs due to low complexity
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_length = 0
        
        while left<len(s):
            right=left+1
            substring = ''
            while (right<len(s)) and (s[right] not in substring) and (s[left]!=s[right]):
                right+=1
                substring+= ''.join(s[left:right])
            length = right-left
            if length >max_length :
                max_length = length
            left+=1
        return max_length
