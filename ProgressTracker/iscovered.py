class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        
        for check_element in range(left, right+1):
            covered = False
            for _range in ranges:
                if _range[0] <= check_element <= _range[1]:
                    covered = True
                    break
            if not covered:
                return False
        return True