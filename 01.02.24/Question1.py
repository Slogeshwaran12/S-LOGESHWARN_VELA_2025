"""Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces."""

"logic 1:"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        
        start = 0
        max_length = 0
        char_index_map = {}  # Map to store the index of each character
        
        for end in range(n):
            
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1
            
            
            char_index_map[s[end]] = end
            
            
            max_length = max(max_length, end - start + 1)
        
        return max_length


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  
print(solution.lengthOfLongestSubstring("bbbbb"))  
print(solution.lengthOfLongestSubstring("pwwkew")) 

"logic 2:"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        
        start = 0
        end = 0
        max_length = 0
        char_set = set()  # Set to store unique characters in the current substring
        
        while end < n:
            
            if s[end] not in char_set:
                char_set.add(s[end])
                end += 1
                max_length = max(max_length, end - start)
            else:
                 
                char_set.remove(s[start])
                start += 1
        
        return max_length


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  
print(solution.lengthOfLongestSubstring("bbbbb"))  
print(solution.lengthOfLongestSubstring("pwwkew"))  


        

