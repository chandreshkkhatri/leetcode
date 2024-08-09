from typing import List

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        set_tracker = set([])
        i = 0
        aligned_alphabets = []

        while len(aligned_alphabets) < 26:
            if (key[i] != ' ') and (key[i] not in set_tracker):
                aligned_alphabets.append(key[i])
                set_tracker.add(key[i])
            i += 1
            
        ans = ''

        for idx1, c1 in enumerate(message):
            i = 0
            if c1 != ' ':
                while aligned_alphabets[i] != c1:
                    i+=1
                ans = ans + chr(i+ord('a'))
            else:
                ans += ' '
        
        return ans




if __name__ == "__main__":
    s = Solution()
    print(s.decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"))
