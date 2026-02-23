class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)
        for num in hand:
            start = num
            while counts[start - 1]: #reach the min of the group
                start -=1
            while start <= num:
                while counts[start]: # because there can be multiple starts from same num
                    for i in range(start, start+groupSize): #check if consec nums of groupsize exists
                        if not counts[i]:
                            return False
                        counts[i] -= 1
                start += 1
            
        return True
