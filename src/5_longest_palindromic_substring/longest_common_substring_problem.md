# Longest common substring problem

In computer science, the *longest common substring problem* is to find the longest string that is a substring of two or
more strings. The problem may have multiple solutions. Applications include data deduplication and plagiarism detection.

## Example

----

The longest common substring of the strings "ABABC", "BABCA" and "ABCBA" is string "ABC" of length 3. Other common
substring are "A", "AB", "B", "BA", "BC" and "C".

````
ABABC
  |||
 BABCA
  |||
  ABCBA
````

# Problem definition

----
Given two strings, _*S*_ of length _m_ and _*T*_ of length _n_, find the longest string which is substring of both _*S*_
and _*T*_.

A generalization is the *k-common substring problem*. Given the set of strings `S = {S1,...,Sk}`, where `|Si| = ni`, and
$\sum_{n_{i} = N$. Find for each _*2 <= k <= K*_, the longest strings which occur as substring of at least _k_ strings.

## Algorithms

-----
One can find the lenghts and starting positions of the longest common substrings of _*S*_ and _*T*_ in 