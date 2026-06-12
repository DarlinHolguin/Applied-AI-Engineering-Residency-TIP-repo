

# from typing import List

# nums = [2,7,11,15]
# target = 9

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     print([i, j])

# sol = Solution()
# sol.twoSum(nums, target)

# from typing import List

# s = ["h","e","l","l","o"]

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             temp = s[left]
#             s[left] = s[right]
#             s[right] = temp
#             left = left + 1
#             right = right - 1
# sol = Solution()
# sol.reverseString(s)
# print(s)

# function containsDuplicate(nums) {
#   const seen = new Set();
#   for (let i = 0; i < nums.length; i++) {
#     if (seen.has(nums[i])) {
#       return true;
#     }
#     seen.add(nums[i]);
#   }
#   return false;
# }

# from typing import List

# nums = [1,2,3,1]

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False
# sol = Solution()
# print(sol.containsDuplicate(nums))


class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string = str(x)
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True

sol = Solution()
print(sol.is_palindrome(121))
