#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # return set(b).issubset(set(a))
        count_a = Counter(a)
        count_b = Counter(b)

        for key in count_b:
            if count_b[key] > count_a.get(key, 0):
                return False
        return True
