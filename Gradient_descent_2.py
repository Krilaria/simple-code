import matplotlib.pyplot as plt

loss = []
step = []

loss.append(float(-10))
step.append(float(0.1))
lr = 0.007
bias = float(0.001)

for i in range(10000):
    #print(loss[i], step[i])
    if (loss[i]**2 - 7*loss[i] < (loss[i]-step[i])**2 - 7*(loss[i]-step[i])):
        loss.append(loss[-1] + step[i])
    else:
        loss.append(loss[-1] - step[i])
    step.append(step[-1] / (1+lr))
    if ((i > 3) and (abs(loss[-2]-loss[-1])) < bias ):
        plt.plot(loss)
        plt.plot(step)
        plt.show()
        exit()

plt.plot(loss)
plt.plot(step)
plt.show()