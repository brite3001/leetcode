# Very Slow
# def longestCommonPrefix(strs) -> str:

#     current_longest_prefix = ""
#     words_with_matching_prefix = 0

#     for word in strs:

#         for i in range(len(word) + 1):
#             prefix = word[:i]
#             # print(prefix)

#             for other_word in strs:
#                 if prefix == other_word[:i]:
#                     print(prefix, other_word[:i])
#                     words_with_matching_prefix += 1

#                 # print(words_with_matching_prefix)
#                 if words_with_matching_prefix == len(strs):
#                     current_longest_prefix = prefix

#             words_with_matching_prefix = 0

#     return current_longest_prefix


# print(longestCommonPrefix(["flower", "flower", "flower", "flower"]))

import pprint

pp = pprint.PrettyPrinter(indent=4)


def longestCommonPrefix(strs) -> str:
    from collections import defaultdict

    strs = set(strs)

    prefix_dict = defaultdict(set)
    longest_prefix = ""

    for word in strs:
        for i in range(len(word) + 1):
            prefix = word[:i]
            print(prefix)

            if prefix not in prefix_dict:
                for word2 in strs:
                    if prefix == word2[:i]:
                        print(prefix, word2)
                        prefix_dict[prefix].add(word2)

            if len(prefix_dict[prefix]) == len(strs) and len(prefix) > len(
                longest_prefix
            ):
                longest_prefix = prefix

    return longest_prefix


pp.pprint(longestCommonPrefix(["flower", "flow", "flight"]))
