class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0]
        count_dict = {0:0}
        for i in range(1,n+1):
            count = 0
            while i > 0:
                if count_dict.get(i,0):
                    count+=count_dict[i]
                    break
                if i & 1:
                    count +=1
                i = i >> 1

            count_dict[i] = count
            out.append(count)
        return out
