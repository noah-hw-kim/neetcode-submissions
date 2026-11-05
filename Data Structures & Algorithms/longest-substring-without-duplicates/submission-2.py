"""
substring -> contiguous seq string

Input: s = "zxyzxyz"
Output: 3

max_len = 3

z -> valid. len=1, {z}
zx -> valid. len=2, {z,x}
zxy -> valid. len=3 * {z,x,y}
zxyz -> invalid.
zxyzx -> invalid...

x -> valid.
xy -> valid...

how do we know if there's a duplicate?
*hashset*

constraints
0 <= s.length <= 50,000
s may consist of printable ASCII characters.

approach 1 - O(n^2), O(n)
max_len = 0

iterate s -> index i
    seen = set()
    iterate s from i to the last char of s -> index j
        if s[j] in seen: break
        add s[j] in seen
        update max_len with seen length

return max_len

50k ^ 2 = 2,500,000,000 ~= more than 10^8 

approach 2 - one pass? should be O(nlogn) or O(n), ...
zxyz -> invalid. can we start from 2nd z or need to keep explore from x and why? Nope.

zxyzaxc
 l   r

we don't need to move to 2nd z. We need to move to until the point that hits there's no duplicate.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, len(seen))

        return res

        