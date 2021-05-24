# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        if n <= 10:
            for i in range(n+1):
                if isBadVersion(i):
                    return i
        
        l = 0
        r = n
        
        bad_version = 0
        
        while l <= r:
            mid =  l + (r-l) / 2
            
            if isBadVersion(mid):
                bad_version = mid
                r = mid - 1
            else:
                l = mid +1
             
        print(bad_version)
        
        return bad_version
