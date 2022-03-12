# Longest Palindromic Substring

Given a string `s`, return the _longest palindromic substring_ in `s`.

## Example 1:

````
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer
````

## Example 2:

````
Input: s = "cbbd"
Output: "bb"
````

## Constraints:

- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters

# Solution

## Approach 1: Longest Common Substring

### Common mistake

Some people will be temped to come up with a quick solution, which is unfortunately flawed (however can be corrected
easily):

> Reserse *S* and become *S'*. Find the longest common substring between *S* and *S'*, which must be the longest palindromic substring

This seemed to work, let's see some examples below.

For example, *S* = "caba"m *S'* = "abac".

The longest common substring between *S* and *S'* is "aba", which is the answer.

Let's try another example: *S* = "abacdfgdcaba", *S'* = "abacdgfdcaba".

The longest common substring between *S* and *S'* is "abacd". Clearly, this is not a valid palindrome.

### Algorithm

We could see that the longest common substring method fails when there exists a reversed copy of a non-palindromic
substring in some other part of *S*. To rectify this, each time we find a longest common substring candidate, we check
if the substring's indices are the same as the reversed substring's original indices. If it is, then we attempt to
update the longest palindrome found so far; if not, we skip this and find the next candidate.

This gives us an _O(n^2)_ Dynamic Programming solution which uses _O(n^2)_ space (could be improved to use _O(n)_ space)
. Please read more about [Longest Common Substring](http://en.wikipedia.org/wiki/Longest_common_substring)