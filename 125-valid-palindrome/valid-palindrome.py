class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(ch for ch in s if ch.isalnum()).lower()
        l=0;r=len(s)-1;count=0
        while l<r:
                if s[l]==s[r]:
                    l+=1;r-=1
                else:
                    count=1
                    break
           
        if count==0:
                return True
        else:
                return False
        