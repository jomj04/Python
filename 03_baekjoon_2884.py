# 백준 2884번
H, M = input().split()
H = int(H)
M = int(M)
if M - 45 >= 0:
    M = M - 45
else:
    if H == 0:
        H = 23
        M = M + 15
    else:
        H = H -1 #H-=1
        M = M + 15
print(H, end = ' ')
print(M)
