from PIL import Image
import numpy as np
import math
import time

def getColor(data,r,point,weight):
	# r 模糊半径
	c_x,c_y = point
	min_x = c_x - r
	max_x = c_x + r
	min_y = c_y - r
	max_y = c_y + r
	color = np.array([0,0,0])
	for y in range(min_y,max_y):
		for x in range(min_x,max_x):
			now_x = x
			now_y = y
			# 边缘处理
			if y < 0:
				now_y = -y
			if x < 0:
				now_x = -x
			if y > height - 1:
				now_y = height - 1 - y
			if x > width - 1:
				now_x = width - x - 1
			w = weight[x - min_x][y - min_y]
			point = data[now_x,now_y] * w
			color = color + point
	return color.tolist()

def gaussian_fn(x,y):
    # np.exp 返回自然常数 e 
    # sigma σ 控制"钟形"的宽度 现在设为 1.5
    sigma = 2
    return 1 / (2 * math.pi * sigma ** 2) * np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))

def getWeight(r):
	weight = np.zeros((r * 2,r * 2))
	for y in range(r * 2):
		for x in range(r * 2):
			bias_x  = x - r
			bias_y = y - r
			weight[x][y] = gaussian_fn(bias_x,bias_y)
	total = np.sum(weight)
	weight = weight / total
	return weight


if __name__ == '__main__':
	image = Image.open("test2.jpg")
	width,height = image.size
	total = width * height
	count = 0
	r = 5
	data = np.array(image)
	weight = getWeight(r)
	for y in range(height):
		for x in range(width):
			data[x][y] = getColor(data,r,(x,y),weight)
			count += 1
			print('point %i/%i' % (count,total),end='\r')
	res = Image.fromarray(data)
	res.save("result2.jpg")
