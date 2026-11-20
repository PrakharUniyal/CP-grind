# # TC: O(N^2), SC: O(1)
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]

# TC: O(N), SC: O(N)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ind = dict()
        for i in range(len(nums)):
            if nums[i] in ind:
                ind[nums[i]].append(i)
            else:
                ind[nums[i]] = [i]
        for i in range(len(nums)):
            if target - nums[i] in ind:
                if ind[target - nums[i]][0] != i:
                    return [i,ind[target-nums[i]][0]]
                elif len(ind[target - nums[i]])>1:
                    return [i,ind[target-nums[i]][1]]