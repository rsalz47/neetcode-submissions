class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_letters = defaultdict(lambda: 0)
        t_letters = defaultdict(lambda: 0)

        for letter in s:
            s_letters[letter] += 1

        for letter in t:
            t_letters[letter] += 1

        for letter in s_letters:
            if letter not in t_letters:
                return False
            if s_letters[letter] != t_letters[letter]:
                return False
        
        return True