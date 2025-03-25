s='bbbbb'
left=0
max_length=0
while left<len(s):
    right=left+1
    substring=[]
    length=0
    while (right<len(s)):
        if s[right] not in substring:
            substring.append(s[right])
            right+=1
            length+=1
        else:
            break
    if length>max_length:
        max_length=length
    left+=1
print(max_length)
