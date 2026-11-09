class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums: 
            if num not in seen: 
                seen[num] = 1
            else: 
                seen[num] += 1
        
        buckets = [[] for index in range(len(nums) + 1)]

        for num, freq in seen.items(): 
            buckets[freq].append(num)
        
        answer = []
        for freq in range(len(buckets) -1, 0, -1): 
            for num in buckets[freq]:
                answer.append(num)
            if len(answer) == k: 
                return answer

        

        