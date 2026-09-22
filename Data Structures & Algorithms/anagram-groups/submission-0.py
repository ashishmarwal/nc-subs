class Solution:
    def sortString(self, s: str) -> str:
        chars = list(s)
        chars.sort()
        return ''.join(chars)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for single items lists no processing needed
        if len(strs) == 1: return [strs]

        anagrams_groups: Dict[str, List[str]] = dict()

        for s in strs:
            # sorted
            key = self.sortString(s)
            anagrams_groups.setdefault(key, [])
            anagrams_groups.get(key).append(s)
        
        return [anagrams_groups.get(k) for k in anagrams_groups.keys()]
