class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in nums1:
            found = False
            flag = False

            for j in nums2:
                if j == i:
                    flag = True
                elif flag and j > i:
                    ans.append(j)
                    found = True
                    break

            if not found:
                ans.append(-1)

        return ans


                    
