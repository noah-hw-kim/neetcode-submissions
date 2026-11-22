"""
Constraints:
1 <= nums.length <= 10^4. -> n^2 and less
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

Approach 1:
Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

counter={
1:1
2:2
3:3
}

max heap structure -> add counter with (count:number) -> pop k times
time: O(n) + O(k * unique(n)) -> O(n) as k is within n range
space: O(n)

use min heap as max heap (negation)
(-3,3), (-2,2), (-1,1)


"""

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1
        
        heap = []
        heapq.heapify(heap)

        for num, count in nums_dict.items():
            heapq.heappush(heap, (-count,num))
        
        res = []
        for i in range(k):
            ct, num = heapq.heappop(heap)
            res.append(num)

        return res
            