from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) #creates empty array
        for s in strs:
            key = "".join(sorted(s)) # sorts their letters
            groups[key].append(s)
        return list(groups.values())
