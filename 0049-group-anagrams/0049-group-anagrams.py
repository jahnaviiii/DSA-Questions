from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            s = "".join(sorted(string))
            if s in res:
                res[s].append(string)
            else:
                res[s] = [string]
        
        return list(res.values())
        