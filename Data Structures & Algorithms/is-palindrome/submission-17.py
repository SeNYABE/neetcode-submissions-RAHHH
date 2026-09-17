import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_trans = str(re.sub(r'[^a-zA-Z0-9]', '', s)).lower()


        i,j = 0,len(s_trans) -1
   
        while j > i :
            if (s_trans[i] == s_trans[j]):
                i +=1
                j -=1
            else:
                return False
        return True