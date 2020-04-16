#### Problem 6: Unsorted Integer Array

We traversed through the integers array only once (single traversal) and while iterating through integers list, we created two variables min_int and max_int which gets updated each time if the current number is larger and/or minimum than the iterator respectively. Therefore, our time complexity for this solution would be big-O of O(n). However, space this method uses is constant i.e (this method don't use extra space if the input size increases) so space complexity is O(1).

- Time complexity: O(n)
- Space complexity: O(1)