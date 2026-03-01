class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        seen = {0:1}
        
        for num in nums:
            current_sum += num
                
            if current_sum - k in seen:
                count += seen[current_sum - k]
                
            seen[current_sum] = seen.get(current_sum, 0) + 1
            
        return count