"""
Constraints:
0 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7

Approach1:
Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4

nums_set = {2,20,4,10,3,4,5} => O(n) * O(n) * O(1) => O(n^2)
 
2 -> 3 -> 4 -> 5 -> 6 x
20 -> 21 x
4 -> 5 -> 6 x
10 -> 11 x

nums_set = {1,2,3,4,5}
1 -> 2 -> 3 -> 4 -> 5 -> 6 x
2 -> 3 -> 4 -> 5 -> 6 x
...

we need to improve which num to check?
potential numbers == cur_num - 1 not in the set

remain only potential numbers and iterate num checks -> but how this gurantee be O(n) time though => O(n) and O(n)?

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        potential_nums = []

        for num in nums_set:
            if num - 1 not in nums_set:
                potential_nums.append(num)

        res = -float("inf")

        for potential_num in potential_nums:
            ct = 1
            while potential_num + 1 in nums_set:
                ct += 1
                potential_num += 1

            res = max(res, ct)

        return res



        