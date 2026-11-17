class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current = 0
        longest = 0
        numSet = set(nums)
        for number in nums: 
            if (number - 1) not in numSet: 
                current = 0
                while (number + current) in numSet: 
                    current += 1
            longest = max(longest, current) 

        return longest               
            