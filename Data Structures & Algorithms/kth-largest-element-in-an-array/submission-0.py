class Solution:
    def findKthLargest(self, nums, k):
        k = len(nums) - k

        def quickselect(l, r):
            p = nums[r]
            i = l

            for j in range(l, r):
                if nums[j] <= p:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[r] = nums[r], nums[i]

            if i == k:
                return nums[i]
            if i < k:
                return quickselect(i + 1, r)
            return quickselect(l, i - 1)

        return quickselect(0, len(nums) - 1)