keep=input()
ans=0
maxans=0
minans=101
for i in keep.split():
    maxans=max(int(i),maxans)
    minans=min(int(i),minans)
    if int(i)<60:
        ans+=1
print(ans) 
print("最大值:",maxans,";最小值:",minans)