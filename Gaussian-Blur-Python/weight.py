import numpy as np
import math
size = (3,3)
point = (1,1)
weight = np.zeros(size)
def gaussian_fn(x,y):
    # np.exp 返回自然常数 e 
    # sigma σ 控制"钟形"的宽度 现在设为 1.5
    sigma = 1.5
    return 1 / (2 * math.pi * sigma ** 2) * np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))

for y in range(size[0]):
	for x in range(size[1]):
		bias_x  = x - point[0]
		bias_y = y - point[1]
		print(bias_x,bias_y)
		weight[x][y] = gaussian_fn(bias_x,bias_y)

total = np.sum(weight)
weight = weight / total