# 백준 15552번 문제 (빠른 입출력 관련)
import sys
T = int(sys.stdin.readline().rstrip())
result = []
for x in range(T):
    nums = map(int, sys.stdin.readline().rstrip().split())
    result.append(sum(nums))
for x in result:
    print(x, end = ' ')
