n = int(input())
positions = list(map(int,input().split()))
positions.sort()
optimal = positions[(n-1)//2]
print(optimal)
