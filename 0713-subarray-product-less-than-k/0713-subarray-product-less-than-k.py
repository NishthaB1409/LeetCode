class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        count = 0
        prod = 1
        left = 0

        for i in range(len(nums)):
            prod *= nums[i]
            while (prod >= k):
                prod //=nums[left]
                left += 1

            count = count + (i - left + 1)

        return count
