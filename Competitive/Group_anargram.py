# https://leetcode.com/problems/group-anagrams/description/


def groupAnagrams(strs):
    h = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in h:
            h[sorted_word].append(word)
        else:
            h[sorted_word] = [word]
    
    res = []
    for value in h.values():
        res.append(value)

    return res

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
#[["bat"],["nat","tan"],["ate","eat","tea"]]