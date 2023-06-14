s = input().split()
for i in range(len(s)-1,-1,-1):
    if i ==0:
       print(s[i])
    else:    
        print(s[i],end=' ')
