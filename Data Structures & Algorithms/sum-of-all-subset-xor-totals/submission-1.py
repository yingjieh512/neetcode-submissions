class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(index, current_xor):
            nonlocal res
            if index==len(nums):
                res+=current_xor
                return
            backtrack(index+1,current_xor^nums[index])
            backtrack(index+1,current_xor)
        backtrack(0,0)

        return res