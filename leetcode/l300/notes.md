Leetcode 300 - Longest Increasing Subsequence

- Topdown DP approach, DFS with memoization
- Base Case: f(0) = 0, as empty sequence is length 0
- General Case: f(i) = max(f(0), f(1), ... , f(j)) for j =      0 ... i
  - 1 as long as nums[j] < nums[i]
- State: f(i) is the longest increasing subsequence containing nums[i]