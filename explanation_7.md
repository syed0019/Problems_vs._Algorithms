#### Problem 7: Request Routing in a Web Server with a Trie

Here we dealt with a sequence data/network nodes using Trie data structures. We iterated through each part of the paths and created new TrieNode for each path therefore our both time and space complexities in terms of handler method is O(n). As for the lookup method, we iterated through each path to search/lookout, hence time complexity of O(n), but for the space complexity it is big-O of O(1) as no additional memory is allocated.

_Handler Method:_
- Time complexity: O(n)
- Space complexity: O(n)

_Lookup Method:_
- Time complexity: O(n)
- Space complexity: O(1)