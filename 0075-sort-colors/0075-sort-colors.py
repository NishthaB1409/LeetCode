class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        k = 0
        j = n-1
        i = 0
        while k <= j:
            if nums[k] == 2:
                t = nums[k]
                nums[k] = nums[j]
                nums[j] = t
                j = j - 1
            elif nums[k] == 0:
                r = nums[k]
                nums[k] = nums[i]
                nums[i] = r
                i = i + 1
                k = k + 1
            else:
                k = k + 1


