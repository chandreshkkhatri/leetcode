
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        good_pair_counter = 0
        for num1 in nums1:
            for num2 in nums2:
                if num1%(num2*k) == 0:
                    good_pair_counter += 1
        
        return good_pair_counter
    

if __name__ == "__main__":
    s = Solution()
    print(s.numberOfPairs(nums1 = [3,1,2,2], nums2 = [1,1,1,1], k = 3))