# Longest Substring Without Repeating Characters

----------

Given a string `s`, find the length of the __longest substring__ without repeating characters.

## Example 1:

----

````
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
````

## Example 2:

----

````
Input: s = "bbbbbb"
Output: 1
Explanation: The answer is "b", with the lenght of 1.
````

## Example 3:

----

````
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a sequence and not a substring.
````

## Constraints:

----

* `0 <= s.length <= 5e4`
* `s` consists of English letters, digits, symbols and space.

**The desire time complexity is O(n) where n is the length of the string.**

### Method 1 (Simple: O(n^3))

----

We can consider all substrings one by one and check for each substring whether it contains all unique characters or not.
There will be `n*(n+1)/2` substrings. Whether a substring contains all unique characters or not can be checked in linear
time by scanning it from left to right and keeping a map of visited characters. Time complexity of this solution would
be O(n^3).

````python
def are_distinct(s: str, i, j):
    """"This function returns true if all
     characters in s[i..j] are distinct,
      otherwise return false
    """""
    # Note: Default values in visited are false
    visited = [0] * (26)

    for k in range(i, j + 1):
        if visited[ord(s[k]) - ord('a')] is True:
            return False
        visited[ord(s[k]) - ord('a')] = True

    return True

def longest_unique_substring(s: str) -> int:
    """"
    Returns length of the longest substring
     with all distinct characters
     """""
    n = len(s)
    # Result
    res = 0

    for i in range(n):
        for j in range(i, n):
            if are_distinct(s, i, j):
                res = max(res, j - i + 1)

    return res
````

### Method 2 (Better: O(n^2))

----

The idea is to use window sliding. Whether we see repetition, we remove the previous occurrence and slide the window.

````python
def longet_unique_substring(s: str) -> int:
    n = len(s)
    # Result
    res = 0
    for i in range(n):
        # Note: Default values in visited are false
        visited = [0] * 256
        
        for j in range(i, n):
            # If current character is visited
            # break the loop
            if (visited[ord(s[j])] == True):
                break
            # Else update the result if this 
            # window is larger, and mark 
            # current character are visited.
            else:
                res = max(res, j - i + 1)
                visited[ord(s[j])] = True

        # Remove the first character of previous  window
        visited[ord(s[i])] = False

    return res
````

### Method 3 (Linear Time)

---

Using this solution the problem can be solved in linear time using the window sliding technique. Whether we see
repetition, we remove the window till the repeated string.

````python
def longest_unique_substring(s: str) -> int:
    test = ""
    # Result
    max_length = -1

    # Return 0 if s is empty
    # or 1 if lenght of string is 1
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    
    for c in s:
        if c in test:
            test = test[:test.index(c) - 1]
        test = test + c
        max_length = max(len(test), max_length)
    
    return max_length    
````
