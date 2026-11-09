class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums: 
            if num not in seen: 
                seen[num] = 1
            else: 
                seen[num] += 1
        answer = []
        for i in range(k): 
            max_key = max(seen, key=seen.get)
            answer.append(max_key)
            seen.pop(max_key)

        return answer
        

        