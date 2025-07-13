def rem_dulpicate(s):
    if len(s)<=1:
        return s
    else:
        s[0]==s[1:]
        return s[0]+rem_dulpicate(len(s)-1)
res=rem_dulpicate("hello")
print(res)