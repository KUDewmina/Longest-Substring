class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_lenght = 0
        possible_subs = set()
        n = len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                possible_subs.add(s[i:j])
        new_subs = set()
        for i in possible_subs:
            for index,j in enumerate(i):
                if j in (i[index+1:] or i[:index]):
                    break
            else:
                new_subs.add(i)
        for sub in new_subs:
            if len(sub)>max_lenght:
                max_lenght = len(sub)
        return max_lenght
        
