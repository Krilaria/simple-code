from matplotlib import pyplot as plt 

print('Enter start x')
x=float(input()) 
print('Enter step (0.1 is good)')
a=float(input())

curr_x=[]
curr_i=[]

#function y=x**2+20*x

#gradient descent
for i in range(50):
    curr_x.append(x)
    curr_i.append(i)
    yy=2*x+20
    x-=a*yy
    #print(x)    

#typecasning list
curr_x= [float(j) for j in curr_x]

#plotting the graph
plt.plot(curr_i, curr_x)
plt.title("Finding minimum")
plt.grid()
plt.show()