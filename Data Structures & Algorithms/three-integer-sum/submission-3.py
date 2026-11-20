"""
Example 1
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

-1 0 1 == 0 -> O
-1 0 2 != 0 -> X
...
-1 0 -4 != 0 -> X

-1 1 2 != 0 -> X
...

-1 2 -1 == 0 -> O
...

0 1 -1 == 0 -> O (duplicate)

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

approach
1. three pointers - O(n^3), O(?)
use i,j,k pointers to find combinations
-> once find a combination, check for the duplicate with a set
-> then put duplicate free tuples into the final list

-1 0 1 -> [-1,0,1] -> (-1,0,1)
-1 2 -1 -> [-1,-1,2] -> (-1,-1,2)
0 1 -1 -> [-1,0,1] -> (-1,0,1)

set = {}

2. two pointers -
Example 1
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

sorted_nums = [-4,-1,-1,0,1,2]
1st number = -4
find combination: -1 + 2, -1 + 2, 0 + 2, 1 + 2
-> not found

2nd nubmer = -1
find combination: -1 + 2, 0 + 2, 0 + 1..
-> found [-1,-1,2], [-1,0,1]

3rd number = -1
find combination: 0 + 2, 0 + 1
-> found [-1,0,1] duplicate. We need to prevent the duplicate

* When moving the 1st pointers, skip if it's same as the previous number -> prevent duplicate

sorted_nums = [-4,-1,-1,0,1,1,2]

* When moving the 2nd pointers when it found the answer, skip if it's same as the previous number -> prevent duplicate

sorted_nums = [-4,-1,-1,0,1,2]
i = 1
l = 2
r = 5

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            
        return res
        