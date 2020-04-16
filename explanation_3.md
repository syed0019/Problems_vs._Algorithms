#### Problem 3: Rearrange Array Digits

In this problem, I decided to utilize mergesort algorithm to arrive at the solution. Considering the mergesort efficiency, the number of steps/iterations made (log(n)) to search for the numbers in both left and right sides of the array and number of comparisons made at each steps (n), this results in time complexity of O(n * log(n)) or simply O(nlog(n)). As for the space complexity, the auxillary/extra space used to create the new lists which is linear, this results in space complexity of O(n). 

- Time complexity: O(nlog(n))
- Space complexity: O(n)