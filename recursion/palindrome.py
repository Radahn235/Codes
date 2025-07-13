def is_palindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
res=is_palindrome("madam")
print(res) 