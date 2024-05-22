from collections import defaultdict
from bisect import bisect_left

s = input()
letter_log = defaultdict(list)

for i in range(len(s)):
    letter_log[s[i]].append(i)

for test in range(int(input())):
    w = input()
    longest_suffix = 0
    position = len(s)
    for i in range(len(w)-1,-1,-1):
        c = w[i]
        if not letter_log[c]:
            break
        index = bisect_left(letter_log[c], position)
        if index == 0:
            break
        position = letter_log[c][index-1]
        longest_suffix += 1
    print(longest_suffix)


# s = input()
# character_last_found = [None]*26
# log = []

# for i in range(len(s)):
#     log.append(character_last_found[:])
#     character_last_found[ord(s[i])-97] = i

# log.append(character_last_found[:])

# for test in range(int(input())):
#     w = input()
#     longest_suffix = 0
#     position = len(s)
#     for i in range(len(w)-1,-1,-1):
#         c = ord(w[i])-97
#         if log[position][c] is None:
#             break
#         else:
#             position = log[position][c]
#             longest_suffix += 1
#     print(longest_suffix)


# # Create trie of all the substrings less than length 5*10^4 of the given string and then search for the given string in the trie.

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.endOfString = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert_substrings(self, string):
#         for i in range(len(string)):
#             for j in range(i+1, min(i+1+5*10**4, len(string)+1)):
#                 self.insert(string[i:j])

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.endOfString = True

#     def search(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.endOfString

# # Usage
# trie = Trie()
# trie.insert_substrings(input())

# # # Print alla the words in the trie
# # def print_all_words(node, word):
# #     if node.endOfString:
# #         print(word)
# #     for char in node.children:
# #         print_all_words(node.children[char], word+char)

# # print_all_words(trie.root, "")

# # binary search for longest suffix of a string that is in the trie
# def binary_search(trie, string):
#     left = 0
#     right = len(string)
#     while left < right:
#         mid = (left+right+1)//2
#         if trie.search(string[-mid:]):
#             left = mid
#         else:
#             right = mid-1
#     return left

# for test in range(int(input())):
#     print(binary_search(trie, input()))