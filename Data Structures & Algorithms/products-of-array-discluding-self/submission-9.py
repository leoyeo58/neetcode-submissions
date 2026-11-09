class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left = 1 
        for index in range(len(nums)): 
            output[index] = left
            left *= nums[index]

        right = 1
        for index in range(len(nums)-1, -1, -1): 
            output[index] *= right
            right *= nums[index]
        
        return output


        