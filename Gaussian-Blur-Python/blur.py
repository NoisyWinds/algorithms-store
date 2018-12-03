from PIL import Image
import numpy as np
import time
image = Image.open("test.jpg")
width,height = image.size
total = width * height
count = 0
data = np.array(image)
def getColor(r,point):
	# r 模糊半径
	c_x,c_y = point
	min_x = c_x - r
	max_x = c_x + r
	min_y = c_y - r
	max_y = c_y + r
	if min_x < 0:
		min_x = 0
	if max_x > width:
		max_x = width
	if min_y < 0:
		min_y = 0
	if max_y > height:
		max_y = height
	r = 0
	g = 0
	b = 0
	count = 0
	for x in  range(min_x,max_x):
		for y in range(min_y,max_y):
			if x == c_x and y == c_y:
				continue
			r += data[x][y][0]
			g += data[x][y][1]
			b += data[x][y][2]
			count += 1
	return (round(r / count),round(g / count),round(b / count))

t1 = time.time()
for y in range(height):
	for x in range(width):
		data[x][y] = getColor(5,(x,y))
		count += 1
		print('point %i/%i' % (count,total),end='\r')
res = Image.fromarray(data)
res.save("result.jpg")
t2 = time.time()
print('\r')
print('time:%is' % (t2 - t1))
print('image saved result.jpg')