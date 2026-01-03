class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for key in freq.keys():
            if freq[key] > n/2:
                return key

    


                

                
