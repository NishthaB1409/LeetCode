class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
                    ans = []

                    for i in range(1, numRows + 1):
                        row = []
                        for j in range(i):
                            if j == 0 or j == i - 1:
                                row.append(1)
                            else:
                                if i > 2:
                                    row.append(ans[i - 2][j - 1] + ans[i - 2][j])
                        ans.append(row)

                    return ans
