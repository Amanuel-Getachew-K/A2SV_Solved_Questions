class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(sbarry,k):
            i = 0
            while i < k // 2:
                sbarry[i] , sbarry[k-i-1] = sbarry[k-i-1],sbarry[i]
                i += 1
            
        value = len(arr)
        ans = []
        while value > 0:
            idx = arr.index(value)

            if idx != value - 1:
                if idx != 0:
                    ans.append(idx+1)
                    flip(arr,idx+1)
                ans.append(value)
                flip(arr,value)

            value -= 1

        return ans
