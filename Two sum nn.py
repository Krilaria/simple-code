nums=input().split()
target=int(input())
v=[]
ind=[-1,-1]

nums=[int(i) for i in nums]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        v.append(nums[i]+nums[j])
        if v[-1]==target:
            ind[0]=i
            ind[1]=j
            break

print(ind)