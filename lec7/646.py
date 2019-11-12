class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        #贪心算法
        if not pairs:
            return 0
        pairs.sort(key=lambda x: x[1])
        count = 1
        cur = pairs[0][1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > cur:
                count += 1
                cur = pairs[i][1]
        return count