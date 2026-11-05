"""
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Anagram -> can make a same word by rearrange letters

h 1
a 1 -> "hat"
t 1

a 1
c 1 -> act, cat
t 1

s 1
t 1
o 1 -> stop, pots, tops
p 1

constraints:
    strs have at least one item
    strs[i] can be an empty str
    strs[i] only lowercase

approach
1. brute force
if we can make a matching key using # of letter and type of a letter than we can use something like a dictionary. We need to figure out how to make this matching key

a1c1t1: ["act"]
p1o1t1s1: ["pots"]

str -> create a counter from it -> check if this counter is exist in dict (hard) -> put it there

* dict key can't be dict. Only tuple, integer, str, ...
We need to change the counter form to a tuple? can we do this?
* if tuple, we need to have a same form for pots and stop. order and make a tuple?

first str
h:1
a:1
t:1

-> get only keys. sort them. create a tuple with the sortedkey + value

save in the global dict as tuple_counter:[here]





"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_to_str_list = {}

        for word in strs:
            temp_counter = {}
            for s in word:
                if s not in temp_counter:
                    temp_counter[s] = 0
                temp_counter[s] += 1

            sorted_key = sorted(temp_counter.keys())
            counter_str = ""
            
            for key in sorted_key:
                counter_str = counter_str + key + str(temp_counter[key])

            if counter_str not in counter_to_str_list:
                counter_to_str_list[counter_str] = []

            counter_to_str_list[counter_str].append(word)

        res = []

        # for counter in counter_to_str_list:

        for str_list in counter_to_str_list.values():
            res.append(str_list)

        return res



        