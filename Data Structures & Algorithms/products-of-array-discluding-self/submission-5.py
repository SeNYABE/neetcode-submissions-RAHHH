class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product everything except 0,      
        res = []
        
        # 1. Count how many zeros exist
        zero_count = nums.count(0)
        
        # 2. Calculate the product of all non-zero numbers
        total = math.prod(num for num in nums if num != 0)
        
        # 3. Build the result based on zero count
        for i in nums:
            if zero_count > 1:
                # Multiple zeros mean every single product will be 0
                res.append(0)
            elif zero_count == 1:
                # One zero: only the zero's index gets the total product
                res.append(total if i == 0 else 0)
            else:
                # No zeros: standard integer division
                res.append(total // i)
                
        return res
