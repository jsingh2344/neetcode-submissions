class Solution:

    def toDictTuple(self, word):

        d = {}

        for letter in word:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
        
        return tuple(sorted(d.items()))


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_of_dicts = {} #dictionary of anagram keys (dicts) that map to indices

        for word in strs:

            dict_word = self.toDictTuple(word)
            if dict_word in dict_of_dicts:
                dict_of_dicts[dict_word].append(word)
            else:
                dict_of_dicts[dict_word] = [word]

        res = []
        for key in dict_of_dicts:
            res.append(dict_of_dicts[key])

        return res



