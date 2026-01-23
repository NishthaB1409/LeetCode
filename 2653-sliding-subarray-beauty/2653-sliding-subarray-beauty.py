from typing import List

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = [0] * 101  # counts for values -50 to 50
        res = []

        def add(v):
            cnt[v + 50] += 1

        def remove(v):
            cnt[v + 50] -= 1

        def beauty():
            need = x
            for v in range(-50, 0):
                freq = cnt[v + 50]
                if need <= freq:
                    return v
                need -= freq
            return 0

        # initialize first window
        for i in range(k):
            add(nums[i])

        res.append(beauty())

        # slide the window
        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i - k])
            res.append(beauty())

        return res
