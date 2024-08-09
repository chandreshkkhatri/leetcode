from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        attr = []
        n = len(names)
        for i in range(n):
            attr.append({"name": names[i], "height": heights[i]})

        ans = sorted(attr, key=lambda d: d.get("height"), reverse=True)
        return [person["name"] for person in ans]
    
if __name__ == "__main__":
    s = Solution()
    print(s.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))