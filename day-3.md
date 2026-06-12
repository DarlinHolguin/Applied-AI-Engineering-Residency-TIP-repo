# Day 3

```js
function reverseString(s) {
  let left = 0;
  let right = s.length - 1;
  while (left < right) {
    let temp = s[left];
    s[left] = s[right];
    s[right] = temp;
    left++;
    right--;
  }
  return s;
}
```

```py
from typing import List

s = ["h","e","l","l","o"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left + 1
            right - 1=
            print(s)

sol = Solution()
sol.reverseString(s)
```
