a = int(input())
gate = int(input())
b = int(input())
max_time = int(input())
if b>max_time and a+gate>max_time:
    print("no delivery")
elif a+gate<b:
    print("A")
else:
    print("B")
