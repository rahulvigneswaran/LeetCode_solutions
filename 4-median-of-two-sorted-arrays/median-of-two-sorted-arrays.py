class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        
        total = len(A) + len(B)
        half = total // 2
        L = 0
        R = len(A) - 1
        while True:
            m_A = (L + R) // 2 # A
            m_B = half - m_A - 2

            # A
            ALeft = A[m_A] if m_A >= 0 else float("-inf")
            ARight = A[m_A + 1] if m_A + 1 < len(A) else float("inf")
            # B
            BLeft = B[m_B] if m_B >= 0 else float("-inf")
            BRight = B[m_B + 1] if m_B + 1 < len(B) else float("inf")

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 == 1: #Odd
                    return min(ARight, BRight)
                else: #Even
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                R = m_A - 1
            else:
                L = m_A + 1
    
                