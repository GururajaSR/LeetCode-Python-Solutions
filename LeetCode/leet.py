# LeetCode Questions and Solutions

# 1. Two Sum
# Given an array of integers nums and an integer target, return the indices of the two numbers 
# such that they add up to target. You may assume that each input would have exactly one solution, 
# and you may not use the same element twice. You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the list 'nums' that add up to 'target' and return their indices.

        Args:
        nums (List[int]): List of integers.
        target (int): The target sum.

        Returns:
        List[int]: Indices of the two numbers that add up to the target.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Test cases
nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))  # Output: [0, 1]

nums1 = [3, 2, 4]
target1 = 6
print(Solution().twoSum(nums1, target1))  # Output: [1, 2]

nums2 = [3, 3]
target2 = 6
print(Solution().twoSum(nums2, target2))  # Output: [0, 1]


# 2. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the 
# value to go outside the signed 32-bit integer range, then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse the digits of the given integer 'x'.

        Args:
        x (int): The integer to be reversed.

        Returns:
        int: The reversed integer, or 0 if it exceeds 32-bit integer range.
        """
        if x == 0:
            return 0
        elif x > 0:
            reversed_x = int(str(x)[::-1])
        else:
            reversed_x = -int(str(-x)[::-1])
        
        # Check for 32-bit integer overflow
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        return reversed_x

# Test cases
x = 123
print(Solution().reverse(x))  # Output: 321

x = -123
print(Solution().reverse(x))  # Output: -321

x = 120
print(Solution().reverse(x))  # Output: 21


# 3. Palindrome Number
# Given an integer x, return true if x is a palindrome integer. An integer is a palindrome when 
# it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Check if the given integer 'x' is a palindrome.

        Args:
        x (int): The integer to be checked.

        Returns:
        bool: True if 'x' is a palindrome, False otherwise.
        """
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

# Test cases
x = -121
print(Solution().isPalindrome(x))  # Output: False

x = 121
print(Solution().isPalindrome(x))  # Output: True

x = 10
print(Solution().isPalindrome(x))  # Output: False


# 4. Integer to Roman
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Given an integer, convert it to a roman numeral.

class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert the given integer 'num' to a Roman numeral.

        Args:
        num (int): The integer to be converted.

        Returns:
        str: The Roman numeral representation of the integer.
        """
        roman_numerals = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        roman_str = ''
        for value, symbol in roman_numerals.items():
            while num >= value:
                roman_str += symbol
                num -= value
        return roman_str

# Test cases
num = 3
print(Solution().intToRoman(num))  # Output: "III"

num = 58
print(Solution().intToRoman(num))  # Output: "LVIII"

num = 1994
print(Solution().intToRoman(num))  # Output: "MCMXCIV"


# 5. Roman to Integer
# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert the given Roman numeral 's' to an integer.

        Args:
        s (str): The Roman numeral to be converted.

        Returns:
        int: The integer representation of the Roman numeral.
        """
        roman_to_int = {
            'M': 1000, 'D': 500, 'C': 100, 'L': 50,
            'X': 10, 'V': 5, 'I': 1
        }
        num = 0
        prev_value = 0
        for char in reversed(s):
            value = roman_to_int[char]
            if value < prev_value:
                num -= value
            else:
                num += value
            prev_value = value
        return num

# Test cases
s = "III"
print(Solution().romanToInt(s))  # Output: 3

s = "LVIII"
print(Solution().romanToInt(s))  # Output: 58

s = "MCMXCIV"
print(Solution().romanToInt(s))  # Output: 1994


# 6. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings. 
# If there is no common prefix, return an empty string "".

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix string among the list of strings.

        Args:
        strs (List[str]): List of strings.

        Returns:
        str: The longest common prefix.
        """
        if not strs:
            return ""
        
        # Find the shortest string
        min_str = min(strs, key=len)
        
        for i in range(len(min_str)):
            for s in strs:
                if s[i] != min_str[i]:
                    return min_str[:i]
        return min_str

# Test cases
strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))  # Output: "fl"

strs = ["dog", "racecar", "car"]
print(Solution().longestCommonPrefix(strs))  # Output: ""


# 7. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Args:
        s (str): The input string.

        Returns:
        int: The length of the longest substring without repeating characters.
        """
        char_index_map = {}
        start = 0
        max_length = 0
        
        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            char_index_map[char] = i
            max_length = max(max_length, i - start + 1)
        
        return max_length

# Test cases
s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))  # Output: 3

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))  # Output: 1

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))  # Output: 3


# 8. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the array which give the sum of zero.

        Args:
        nums (List[int]): List of integers.

        Returns:
        List[List[int]]: List of unique triplets that sum up to zero.
        """
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return result

# Test cases
nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]


# 9. 3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers in nums 
# such that the sum is closest to target. Return the sum of the three integers.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Find the sum of three integers in the array that is closest to the target.

        Args:
        nums (List[int]): List of integers.
        target (int): The target sum.

        Returns:
        int: The sum of the three integers closest to the target.
        """
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        
        return closest_sum

# Test cases
nums = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumClosest(nums, target))  # Output: 2


# 10. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
# that the number could represent. Return the answer in any order.

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Return all possible letter combinations that the number could represent.

        Args:
        digits (str): String of digits.

        Returns:
        List[str]: List of letter combinations.
        """
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        def backtrack(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return
            for letter in phone_map[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        combinations = []
        backtrack(0, [])
        return combinations

# Test cases
digits = "23"
print(Solution().letterCombinations(digits))  # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


# 11. 4Sum
# Given an array nums of n integers and an integer target, return all unique quadruplets [nums[a], nums[b], nums[c], nums[d]] 
# such that i != j != k != l, and nums[a] + nums[b] + nums[c] + nums[d] == target.

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Find all unique quadruplets in the array that sum up to the target.

        Args:
        nums (List[int]): List of integers.
        target (int): The target sum.

        Returns:
        List[List[int]]: List of unique quadruplets that sum up to the target.
        """
        nums.sort()
        result = []
        
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        
        return result

# Test cases
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(Solution().fourSum(nums, target))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]


# 12. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
# An input string is valid if the brackets are closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Check if the given string 's' containing brackets is valid.

        Args:
        s (str): The input string.

        Returns:
        bool: True if the string is valid, False otherwise.
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack

# Test cases
s = "()"
print(Solution().isValid(s))  # Output: True

s = "()[]{}"
print(Solution().isValid(s))  # Output: True

s = "(]"
print(Solution().isValid(s))  # Output: False


# 13. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of well-formed parentheses.

        Args:
        n (int): Number of pairs of parentheses.

        Returns:
        List[str]: List of all combinations of well-formed parentheses.
        """
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        
        result = []
        backtrack()
        return result

# Test cases
n = 3
print(Solution().generateParenthesis(n))  # Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

