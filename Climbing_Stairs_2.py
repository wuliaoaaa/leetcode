class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        list_n = [1, 2]
        i = 2
        while i < n:
            list_n.append(list_n[i-1] + list_n[i-2])
            i = i + 1
        return list_n[n-1]
