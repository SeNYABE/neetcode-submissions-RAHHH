class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list_hash = defaultdict(int)
        for num in nums:
            list_hash[num] +=1
        counter_obj = Counter(list_hash)
        
        return [num for num, f in counter_obj.most_common(k)]