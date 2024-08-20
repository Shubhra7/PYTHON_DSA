from collections import defaultdict

ana = defaultdict(list)

words = [ "cat", "dog", "tac", "god", "act", "z" ]

for word in words:
    ana[''.join(sorted(word))].append(word)

for i in ana.values():
    print(' '.join(i))