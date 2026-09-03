# 1.redefine
# input: nums = int[]
# output: true - any value appears more than once. false - otherwise
# constraints:
#   0 <= nums.length <= 10^5
#   -10^9 <= nums[i] <= 10^9

# 2.examples:

# 3.approach
# 1) brute force - two pointers.
#   start from the first element -> compare with 2nd, 3rd, ...
#   if found a same number, return True
#   once comparing done, return False
#   O(n^2), O(1)

# 2) how about use some more spaces to boost the time efficiency to O(nlogn) or O(n) or more optimized -> hashset
# create an empty set -> nums_set
# iterate number in nums
#   if number is in the nums_set then return true
#   add number in nums_set
# return False



class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force - O(n^2), O(1)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # optimized using more space - O(n), O(n)
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)

        return False


        