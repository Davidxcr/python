def runningSum(self, nums):
    ans = [1, 2, 3]
    tmp = 0
    for i in nums:
        tmp += 1
        ans.append(tmp)
    return ans 