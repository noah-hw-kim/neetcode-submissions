"""
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

nums[0] = nums[1] * nums[2] * nums[3]
nums[1] = nums[0] * nums[2] * nums[3]
nums[2] = nums[0] * nums[1] * nums[3]
nums[3] = nums[0] * nums[1] * nums[2]

2 <= nums.length <= 100,000 (10^5) -> faster than O(n^2)
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

approach 1 - brute force O(n^2), O(n) or O(1) if result list is not counted

res = []

iterate nums -> index i
    cur_num = nums[i]
    iterate nums -> index j
        if i != j then
            cur_num *= nums[j]
    res.append(cur_num)

return res

approach 2 - iterate a fixed number like one pass, two pass, ..., but defined. O(n), O(1) if the answer doesn't count

Input: nums = [1,2,4,6]

get prefix
cur_num = nums[0] (start); 48
res = [1,1,2,8]

iterate nums -> index i, start from index 1
    res[i] *= cur_num
    cur_num *= nums[i]

get suffix
cur_num = nums[len(nums) - 1) (start); 24
res = [48,24,12,8]

iterate nums -> index i, start from index len(nums) - 2
    res[i] *= cur_num
    cur_num *= nums[i]

Output: [48,24,12,8]



"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # prefix
        cur_num = nums[0]

        for i in range(1, len(nums)):
            res[i] *= cur_num
            cur_num *= nums[i]

        # suffix
        cur_num = nums[len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            res[i] *= cur_num
            cur_num *= nums[i]

        return res

        