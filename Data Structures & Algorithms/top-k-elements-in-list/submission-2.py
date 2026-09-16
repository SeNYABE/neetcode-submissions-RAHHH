class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list_hash = {}
        for num in nums:
            if num in list_hash:
                list_hash[num] +=1
            else:
                list_hash[num] = 1
        counter_obj = Counter(list_hash)
        
        return [num for num, f in counter_obj.most_common(k)]