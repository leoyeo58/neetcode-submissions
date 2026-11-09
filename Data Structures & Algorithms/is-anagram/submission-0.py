class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        s_tracker = {}
        t_tracker = {}
        for char in s: 
            if char in s_tracker: 
                s_tracker[char] += 1
            else: 
                s_tracker[char] = 1
        for char in t: 
            if char in t_tracker: 
                t_tracker[char] += 1
            else: 
                t_tracker[char] = 1
        return (s_tracker == t_tracker)
            
        
