# The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
# 01 Test 1
# Input
# Expected output
# 2
# 22
# 2
# 02 Test 2
# Input
# Expected output
# 3
# 333
# 33
# 3
# 03 Test 3
# Input
# Expected output
# 4
# 4444
# 444
# 44
# 4
# 04 Test 4
# Input
# Expected output
# 5
# 55555
# 5555
# 555
# 55
# 5
# 05 Test 5
# Input
# Expected output
# 6
# 666666
# 66666
# 6666
# 666
# 66
# 6
# 06 Test 6
# Input
# Expected output
# 7
# 7777777
# 777777
# 77777
# 7777
# 777
# 77
# 7

n = int(input())
for i in range(n):
    print(str(n) * (n-i))


