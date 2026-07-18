from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = defaultdict(list)

        for word in strs:
            groupDict["".join(sorted(word))].append(word)

        result = []
        for k, v in groupDict.items():
            result.append(v)
        
        return result

