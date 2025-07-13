def rev_string(s):
    if len(s)==0:
        return s 
    else:
        return rev_string(s[1:])+s[0]
res=rev_string("training")
print(res)