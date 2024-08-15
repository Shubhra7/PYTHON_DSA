# Print all Anagrams Together in Python
# Here on this page, we will learn how to Print all Anagrams Together in Python.

# Example :

# Input : wordArr = { “cat”, “dog”, “tac”, “god”, “act”, ”z” }
# Output : cat tac act dog god z
# Explanation : here the output of the current input is cat tac act dog god z as it’s printing all anagrams together

# Link: https://prepinsta.com/python-program/given-a-sequence-of-words-print-all-anagrams-together/



from collections import defaultdict
wordArr = { 'cat', 'dog', 'tac', 'god', 'act', 'z' }

anargrams = defaultdict(list)

for word in wordArr:
    anargrams[''.join(sorted(word))].append(word)

for i in anargrams.values():
    print(' '.join(i))

