class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        if nums_len == 2: return list([0, 1])

        num_indices = {}

        for i in range(nums_len):
            num = nums[i]

            if num_indices.get(str(num)) == None:
                num_indices.setdefault(str(num), [i])
            else:
                num_indices.get(str(num)).append(i)

        # still need a complement
        for i in range(nums_len):
            # Only one valid answer exists
            num = nums[i]
            num_c = target - num

            if (num_c == num):
                n_indices = num_indices.get(str(num))

                if (len(n_indices) > 1):
                    # edge case: target has two values exactly half of it, then the complement would be the same number, so may need to look at the second index
                    return [n_indices[0], n_indices[1]]
            else:
                # look for the presence of the complement
                c_indices = num_indices.get(str(num_c))

                if not c_indices == None:
                    # complement found!
                    return [i, c_indices[0]]
        
        return result





