#### Problem 2: Search in a Rotated Sorted Array

I tried to solve this problem based on BST using divide and conquer strategy and using recursive call to both halves of the array, i.e. one containing numbers less than the target while other one containing numbers greater than target to find the index of the target. Thus, the time complexity for the solution would be big-O of O(log(n)). The space complexity analysis is O(logN) because here solution is recursive and recursive solutions use extra space due to their call stack, i.e. where the result of each call is saved. There are O(log(n)) calls, so the call stack uses O(log(n)) space

- Time complexity: O(log(n))
- Space complexity: O(log(n))