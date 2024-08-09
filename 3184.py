from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cd_counter = 0
        for i in range(len(hours)):
            for j in range(i+1, len(hours)):
                if (hours[i]+ hours[j])%24 == 0:
                    cd_counter += 1

        return cd_counter
    
    
if __name__ == "__main__":
    s = Solution()
    print (s.countCompleteDayPairs([12,12,30,24,24]))