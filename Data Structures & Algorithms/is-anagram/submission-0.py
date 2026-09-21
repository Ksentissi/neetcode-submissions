class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        dict = {}
        for n in s :
            dict[n] = dict.get(n,0) +1
        for n in t :
            dict[n] = dict.get(n,0) - 1

        for value in dict.values():
            if value != 0:
                return False

        return True
        