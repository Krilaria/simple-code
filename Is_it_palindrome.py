w = str(input())
s = int(1)

for i in range(len(w)):
    if w[i] == w[-i-1]:
        s *= 1
    else:
        s *= 0
if s == 0:
    print("No")
else:
    print("Yes")