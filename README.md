# Problems_vs_Algorithms

In this project, I tried solving the seven problems (given below). The questions cover a variety of topics related to the basic algorithms learned in this course.  I tried writing up a clean and efficient answer in Python, as well as a text explanation of the efficiency of both my code and my design choices.

### [Problem 1: Square Root of an Integer](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/problem_1.py)

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is `O(log(n))`


##### [Explanation_1](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/explanation_1.md):
Text explanation of the efficiency of both my code and my design choices.


### [Problem 2: Search in a Rotated Sorted Array](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/problem_2.py)

You are given a sorted array which is rotated at some random pivot point.

Example: `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

`Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4`

##### [Explanation_2](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/explanation_2.md):
Text explanation of the efficiency of both my code and my design choices.


### [Problem 3: Rearrange Array Digits](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/problem_3.py)

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range `[0, 9]`. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.

for e.g. `[1, 2, 3, 4, 5]`

The expected answer would be `[531, 42]`. Another expected answer can be `[542, 31]`. In scenarios such as these when there are more than one possible answers, return any one.

##### [Explanation_3](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/explanation_3.md):
Text explanation of the efficiency of both my code and my design choices.


### [Problem 4: Dutch National Flag Problem](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/problem_4.py)

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: `O(n)` does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an `O(n)` solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:

##### [Explanation_4](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/explanation_4.md):
Text explanation of the efficiency of both my code and my design choices.


### [Problem 5: Autocomplete with Tries](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/problem_5.py)

**Building a Trie in Python**

A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search. Create two classes:

- A `Trie` class that contains the root node (empty string)
- A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

After having a functioning Trie, you need to add the ability to list suffixes to implement autocomplete feature. To do that, you need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.

Using the code written for the `TrieNode`, try to add the suffixes function.

##### [Explanation_5](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/explanation_5.md):
Text explanation of the efficiency of both my code and my design choices.


### [Problem 6: Unsorted Integer Array](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/problem_6.py)

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in `O(n)` time. Do not use Python's inbuilt functions to find min and max.

##### [Explanation_6](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/explanation_6.md):
Text explanation of the efficiency of both my code and my design choices.


### [Problem 7: Request Routing in a Web Server with a Trie](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/problem_7.py)

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

<img src=image.jpg alt="Managing-app-location-with-react-router-2x">

First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node `/`

In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's [SimpleHTTPRequestHandler](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler) which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.

Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character

Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.

More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.

##### [Explanation_7](https://github.com/syed0019/Problems_vs._Algorithms/blob/master/explanation_7.md):
Text explanation of the efficiency of both my code and my design choices.
