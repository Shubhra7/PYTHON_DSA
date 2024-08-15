# Print all Anagrams Together in Python
# Here on this page, we will learn how to Print all Anagrams Together in Python.

# Example :

# Input : wordArr = { “cat”, “dog”, “tac”, “god”, “act”, ”z” }
# Output : cat tac act dog god z
# Explanation : here the output of the current input is cat tac act dog god z as it’s printing all anagrams together

# Link: https://prepinsta.com/python-program/given-a-sequence-of-words-print-all-anagrams-together/


from collections import defaultdict # to create a dictionary
 
#taking the words as input list
words = [ "cat", "dog", "tac", "god", "act", "z" ]

# anagram dictionary
anagrams = defaultdict(list)

# this will check if the words are anagrams of eachother
for word in words:
  anagrams[''.join(sorted(word))].append(word)

# this loop will print all the anagrams together
for anagram in anagrams.values():
  print(' '.join(anagram))
