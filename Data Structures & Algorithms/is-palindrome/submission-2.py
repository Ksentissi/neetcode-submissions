class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = "".join(c for c in s if c.isalnum())
        right = len(clean)-1
        left = 0 
        while left<right :
            if clean[right].lower()!=clean[left].lower() : return False 
            right -=1
            left+=1
        return True
        