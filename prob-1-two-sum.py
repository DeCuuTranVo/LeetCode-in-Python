class Solution:
    def twoSum(self, nums, target):

        ii = 0
        jj = ii + 1
        while ii < len(nums):
            while jj < len(nums):
                # print(ii, jj, target)

                if (nums[ii] + nums[jj] == target):
                    # print("Found it")
                    return [ii, jj]

                jj += 1
            ii += 1
            jj = ii + 1

        return None




if __name__ == "__main__":
    mySolution = Solution()

    # Test 1
    num = [2,7,11,15]
    target = 9
    result = mySolution.twoSum(num, target)
    print(result)

    # Test 2
    nums = [3,2,4]
    target = 6
    result = mySolution.twoSum(nums, target)
    print(result)

    # Test 3
    nums = [3,3]
    target = 6
    result = mySolution.twoSum(nums, target)
    print(result)