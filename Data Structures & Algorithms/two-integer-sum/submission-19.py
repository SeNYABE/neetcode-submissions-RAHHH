class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            
            recip = target - num

            if recip in seen:
                return [seen[recip], i]

            seen[num] = i
        return []

        # for i in range(len(nums)):
        #     if nums[i] > target:
        #         continue

        #     target_recip = target - nums[i]

        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == target_recip:
        #             return [i, j]

        # return []