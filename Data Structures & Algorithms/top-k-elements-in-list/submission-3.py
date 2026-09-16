import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list_hash = {}
        for num in nums:
            if num in list_hash:
                list_hash[num] +=1
            else:
                list_hash[num] = 1
      
        return heapq.nlargest(k, list_hash, key = list_hash.get)