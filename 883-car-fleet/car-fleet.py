class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed))
        res = 0
        for i in range(len(cars)-1, -1, -1):
            if not stack:
                stack.append(cars[i])
            p_1, s_1 = cars[i]
            p_2, s_2 = stack[-1]

            if (target - p_2)/s_2 < (target - p_1)/s_1:
                stack.append(cars[i])
            
        return len(stack)


            

            
        