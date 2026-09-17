import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_trans = str(re.sub(r'[^a-zA-Z0-9]', '', s)).lower()

        i,j = 0,len(s_trans) -1

        while i < j:
            if (s_trans[i] != s_trans[j]):
                return False
            i+=1
            j-=1
        return True