class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0] * (len(nums) + 1)
        for l,r in requests:
            prefix[l] += 1
            prefix[r+1] -= 1
        
        for i in range(len(prefix)):
            prefix[i] += prefix[i-1]

        freq = defaultdict()
        for i in range(len(prefix)-1):
            freq[i] = prefix[i]

        sorted_freq = dict(sorted(freq.items(),key = lambda x : -x[1]))

        vals = copy.deepcopy(nums)
        vals.sort()

        arranged = [0] * len(nums)
        for idx in sorted_freq:
            arranged[idx] = vals.pop()
        
        for i in range(1,len(arranged)):
            arranged[i] += arranged[i-1]

        answer = 0
        for l,r in requests:
            answer += arranged[r] - arranged[l-1] if l > 0 else arranged[r]

        MOD = 10**9 + 7
        return answer % MOD 
