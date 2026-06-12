# Day 5

```js
function isPalindrome(x) {
  if (x < 0) return false;
  const str = x.toString();
  let left = 0;
  let right = str.length - 1;
  while (left < right) {
    if (str[left] !== str[right]) return false;
    left++;
    right--;
  }
  return true;
}
```

```py
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
```
