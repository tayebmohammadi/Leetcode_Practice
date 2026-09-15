class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # groups = defaultdict(list)

        # for word in strs:
        #     key_word = tuple(sorted(word))
        #     groups[key_word].append(word)

        # return list(groups.values())


        lookup = defaultdict(list)

        for word in strs:
            clean = tuple(sorted(word))
            lookup[clean].append(word)
        
        return list(lookup.values())



        