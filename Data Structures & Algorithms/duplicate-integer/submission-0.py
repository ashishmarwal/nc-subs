class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0: return False
        
        seen_nums = list()

        for num in nums:
            if num in seen_nums:
                return True
            else:
                seen_nums.append(num) 
        
        return False
