from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        # counted_a = Counter(a)
        # counted_b = Counter(b)
        # return counted_a == counted_b
        return Counter(a) == Counter(b)