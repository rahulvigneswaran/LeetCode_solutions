class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False

        for i, j, k in triplets:
            x = x or (i == target[0] and j <= target[1] and k <= target[2])
            y = y or (i <= target[0] and j == target[1] and k <= target[2])
            z = z or (i <= target[0] and j <= target[1] and k == target[2])
        
            if x and y and z:
                return True
        
        return False