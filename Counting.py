keep=input()
ans=0
for i in keep.split():
    if int(i)<60:
        ans+=1
print(ans)