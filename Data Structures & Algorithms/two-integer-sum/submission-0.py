class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        if nums_len == 2: return list([0, 1])

        # sorting would loose the order of indices
        # we can go with a complement approach
        for i in range(nums_len):
            num_c = target - nums[i]

            for j in range(i+1, nums_len):
                if (nums[j] == num_c): return list([i, j])

        