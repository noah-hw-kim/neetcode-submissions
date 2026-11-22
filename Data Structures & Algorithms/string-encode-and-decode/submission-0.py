"""
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.

Approach1:
Input: strs = ["Hello","World"]
Output: ["Hello","World"]

if we send with just join
encoded = "HelloWorld"
=> we don't know where to split

if we send with join + special char
encoded = "Hello/World"
=> works but what is the input was ["Hello/","World"]
=> in this case, we need to use very rare special chars or
=> indicate character length?

assume
Input: strs = ["Hello/","World"]
Output: ["Hello","World"]
encoded = "6*Hello/*5World"
=> use length + special char

how to decode?
encoded = "6*Hello/*5World"

1st
cur_idx = 0
delimiter_idx = 1
char_len = int(encoded[cur_idx:delimiter_idx + 1]) = 6
word = encode[delimiter_idx+1:delimiter_idx+char_len+1]

move cur_idx to delimiter_idx+char_len+1
find another delimiter_idx after cur_idx

"""


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded = encoded + str(len(s)) + "*" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        start_idx = 0

        while start_idx < len(s):
            delimiter_idx = s.index("*", start_idx)
            word_len = int(s[start_idx:delimiter_idx])
            word = s[delimiter_idx + 1: delimiter_idx + 1 + word_len]
            decoded.append(word)

            start_idx = delimiter_idx + 1 + word_len
        
        return decoded
        
