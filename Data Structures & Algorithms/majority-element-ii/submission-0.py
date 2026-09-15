class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2, count1, count2 = None, None, 0, 0
        for n in nums:
            if n == c1:
                count1 += 1
            elif n == c2:
                count2 += 1
            elif count1 == 0:
                c1, count1 = n, 1
            elif count2 == 0:
                c2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        
        cnt1, cnt2 = 0, 0
        for n in nums:
            if n == c1:
                cnt1 += 1
            elif n == c2:
                cnt2 += 1
        
        res = []
        thresh = len(nums) // 3
        if cnt1 > thresh:
            res.append(c1)
        if cnt2 > thresh and c2 != c1:
            res.append(c2)
        return res