class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return(False)
        y = str(x)
        z = y[::-1]
        if z == y:
            return(True)
        else: return(False)
        
        