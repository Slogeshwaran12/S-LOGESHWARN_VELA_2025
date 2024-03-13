"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters."""

"logic 1:"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  
print(solution.isAnagram("rat", "car")) 

"logic 2:"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        
        s_freq = {}
        t_freq = {}
        
        
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
        
        
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
        
       
        return s_freq == t_freq


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  
print(solution.isAnagram("rat", "car")) 
