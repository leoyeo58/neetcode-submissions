class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index in range(len(nums)): 
            complement = target - nums[index]
            if complement not in seen: 
                seen[nums[index]] = index
            else:
                return [seen[complement], index]
        