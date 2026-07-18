class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        anaMap = {}
        for ch in s:
            anaMap[ch] = anaMap.get(ch, 0) + 1
        
        for ch in t:
            if ch in anaMap:
                anaMap[ch] -=1
            else:
                return False

        for k, v in anaMap.items():
            if v != 0:
                return False

        return True 