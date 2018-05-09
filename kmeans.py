import numpy as np
import random
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Mengconstruct object x dan y

class obj:
	def __init__(self):
		self.x = random.uniform(0,40)
		self.y = random.uniform(0,35)

# Fungsi untuk visualisasi data

def showDataTraining(c1,c2,c3,c4,c5,c6,data,near,status):
	length = len(data)
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	for i in range(length):
		if (near[i]=="c1"):
			ax.scatter(data[i][0],data[i][1],color='green')
		elif (near[i]=="c2"):
			ax.scatter(data[i][0],data[i][1],color='yellow')
		elif (near[i]=="c3"):
			ax.scatter(data[i][0],data[i][1],color='red')
		elif (near[i]=="c4"):
			ax.scatter(data[i][0],data[i][1],color='blue')
		elif (near[i]=="c5"):
			ax.scatter(data[i][0],data[i][1],color='orange')
		elif (near[i]=="c6"):
			ax.scatter(data[i][0],data[i][1],color='purple')
	ax.scatter(c1.x,c1.y,color='black')
	ax.scatter(c2.x,c2.y,color='black')
	ax.scatter(c3.x,c3.y,color='black')
	ax.scatter(c4.x,c4.y,color='black')
	ax.scatter(c5.x,c5.y,color='black')
	ax.scatter(c6.x,c6.y,color='black')
	if (status=="train"):
		ax.set_title('Data Training')
	elif (status=="test"):
		ax.set_title('Data Testing')
	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	plt.show()

# Fungsi untuk mencari nilai centroid 1 yang baru

def hitungC1Baru(data,near,c1):
	count = 0
	# c1 = obj()
	jumlah = obj()
	jumlah.x = 0
	jumlah.y = 0
	length = len(data)
	for i in range(length):
		if (near[i]=="c1"):
			jumlah.x = jumlah.x + data[i][0]
			jumlah.y = jumlah.y + data[i][1]
			count = count + 1
	if (count>0):
		c1.x = jumlah.x / count
		c1.y = jumlah.y / count
	return c1

# Fungsi untuk mencari nilai centroid 2 yang baru

def hitungC2Baru(data,near,c2):
	count = 0
	# c2 = obj()
	jumlah = obj()
	jumlah.x = 0
	jumlah.y = 0
	length = len(data)
	for i in range(length):
		if (near[i]=="c2"):
			jumlah.x = jumlah.x + data[i][0]
			jumlah.y = jumlah.y + data[i][1]
			count = count + 1
	if (count>0):
		c2.x = jumlah.x / count
		c2.y = jumlah.y / count
	return c2

# Fungsi untuk mencari nilai centroid 3 yang baru

def hitungC3Baru(data,near,c3):
	count = 0
	# c3 = obj()
	jumlah = obj()
	jumlah.x = 0
	jumlah.y = 0
	length = len(data)
	for i in range(length):
		if (near[i]=="c3"):
			jumlah.x = jumlah.x + data[i][0]
			jumlah.y = jumlah.y + data[i][1]
			count = count + 1
	if (count>0):
		c3.x = jumlah.x / count
		c3.y = jumlah.y / count
	return c3

# Fungsi untuk mencari nilai centroid 4 yang baru

def hitungC4Baru(data,near,c4):
	count = 0
	# c4 = obj()
	jumlah = obj()
	jumlah.x = 0
	jumlah.y = 0
	length = len(data)
	for i in range(length):
		if (near[i]=="c4"):
			jumlah.x = jumlah.x + data[i][0]
			jumlah.y = jumlah.y + data[i][1]
			count = count + 1
	if (count>0):
		c4.x = jumlah.x / count
		c4.y = jumlah.y / count
	return c4

# Fungsi untuk mencari nilai centroid 5 yang baru

def hitungC5Baru(data,near,c5):
	count = 0
	# c5 = obj()
	jumlah = obj()
	jumlah.x = 0
	jumlah.y = 0
	length = len(data)
	for i in range(length):
		if (near[i]=="c5"):
			jumlah.x = jumlah.x + data[i][0]
			jumlah.y = jumlah.y + data[i][1]
			count = count + 1
	if (count>0):
		c5.x = jumlah.x / count
		c5.y = jumlah.y / count
	return c5

# Fungsi untuk mencari nilai centroid 6 yang baru

def hitungC6Baru(data,near,c6):
	count = 0
	# c6 = obj()
	jumlah = obj()
	jumlah.x = 0
	jumlah.y = 0
	length = len(data)
	for i in range(length):
		if (near[i]=="c6"):
			jumlah.x = jumlah.x + data[i][0]
			jumlah.y = jumlah.y + data[i][1]
			count = count + 1
	if (count>0):
		c6.x = jumlah.x / count
		c6.y = jumlah.y / count
	return c6

# Fungsi untuk menghitung jarak euclidean dari (x1,y1) ke (x2,y2)

def hitungJarak(x1,y1,x2,y2):
	return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

# Fungsi untuk mereturn list centroid terdekat dari tiap data

def pilihTerdekat(c1, c2, c3, c4, c5, c6, data):
	near = []
	for x in data:
		jarakC1 = hitungJarak(c1.x,c1.y,x[0],x[1]) 
		jarakC2 = hitungJarak(c2.x,c2.y,x[0],x[1])
		jarakC3 = hitungJarak(c3.x,c3.y,x[0],x[1])
		jarakC4 = hitungJarak(c4.x,c4.y,x[0],x[1])
		jarakC5 = hitungJarak(c5.x,c5.y,x[0],x[1])
		jarakC6 = hitungJarak(c6.x,c6.y,x[0],x[1])
		if (jarakC1<jarakC2 and jarakC1< jarakC3 and jarakC1<jarakC4 and jarakC1<jarakC5 and jarakC1<jarakC6):
			near.append("c1")
		elif (jarakC2<jarakC1 and jarakC2< jarakC3 and jarakC2<jarakC4 and jarakC2<jarakC5 and jarakC2<jarakC6):
			near.append("c2")
		elif (jarakC3<jarakC1 and jarakC3< jarakC2 and jarakC3<jarakC4 and jarakC3<jarakC5 and jarakC3<jarakC6):
			near.append("c3")
		elif (jarakC4<jarakC1 and jarakC4< jarakC2 and jarakC4<jarakC3 and jarakC4<jarakC5 and jarakC4<jarakC6):
			near.append("c4")
		elif (jarakC5<jarakC1 and jarakC5< jarakC2 and jarakC5<jarakC3 and jarakC5<jarakC4 and jarakC5<jarakC6):
			near.append("c5")
		elif (jarakC6<jarakC1 and jarakC6< jarakC2 and jarakC6<jarakC3 and jarakC6<jarakC4 and jarakC6<jarakC5):
			near.append("c6")
	return near

# Menghitung nilai SSE dari C1, C2, C3, C4, C5, dan C6

def hitungSSE(c1,c2,c3,c4,c5,c6,data,near):
	sse = 0
	length = len(near)
	for i in range(length):
		if (near[i]=="c1"):
			sse = sse + hitungJarak(c1.x,c1.y,data[i][0],data[i][1])
		elif (near[i]=="c2"):
			sse = sse + hitungJarak(c2.x,c2.y,data[i][0],data[i][1])
		elif (near[i]=="c3"):
			sse = sse + hitungJarak(c3.x,c3.y,data[i][0],data[i][1])
		elif (near[i]=="c4"):
			sse = sse + hitungJarak(c4.x,c4.y,data[i][0],data[i][1])
		elif (near[i]=="c5"):
			sse = sse + hitungJarak(c5.x,c5.y,data[i][0],data[i][1])
		elif (near[i]=="c6"):
			sse = sse + hitungJarak(c6.x,c6.y,data[i][0],data[i][1])
	return sse 

data = np.genfromtxt('TrainsetTugas2.txt')
c1Old = obj()
c2Old = obj()
c3Old = obj()
c4Old = obj()
c5Old = obj()
c6Old = obj()
c1Old.x = 0
c1Old.y = 0
c2Old.x = 0
c2Old.y = 0
c3Old.x = 0
c3Old.y = 0
c4Old.x = 0
c4Old.y = 0
c5Old.x = 0
c5Old.y = 0
c6Old.x = 0
c6Old.y = 0
c1New = obj()
c2New = obj()
c3New = obj()
c4New = obj()
c5New = obj()
c6New = obj()
near = []
near = pilihTerdekat(c1New,c2New,c3New,c4New,c5New,c6New,data)

while (c1Old.x != c1New.x and c1Old.y != c1New.y and c2Old.x != c2New.x and c2Old.y != c2New.y and c3Old.x != c3New.x and c3Old.y != c3New.y and c4Old.x != c4New.x and c4Old.y != c4New.y and c5Old.x != c5New.x and c5Old.y != c5New.y and c6Old.x != c6New.x and c6Old.y != c6New.y):
	c1Old = c1New
	c2Old = c2New
	c3Old = c3New
	c4Old = c4New
	c5Old = c5New
	c6Old = c6New
	c1New = hitungC1Baru(data,near,c1Old)
	c2New = hitungC2Baru(data,near,c2Old)
	c3New = hitungC3Baru(data,near,c3Old)
	c4New = hitungC4Baru(data,near,c4Old)
	c5New = hitungC5Baru(data,near,c5Old)
	c6New = hitungC6Baru(data,near,c6Old)
	near = []
	near = pilihTerdekat(c1New,c2New,c3New,c4New,c5New,c6New,data)

showDataTraining(c1New,c2New,c3New,c4New,c5New,c6New,data,near,"train")
sse = hitungSSE(c1New,c2New,c3New,c4New,c5New,c6New,data,near)
print("SSE = ",sse)
test = np.genfromtxt('TestsetTugas2.txt')
nearTest = []
nearTest = pilihTerdekat(c1New,c2New,c3New,c4New,c5New,c6New,test)
length = len(test)
ans = []
for i in range(length):
	temp = [test[i][0],test[i][1],nearTest[i]]
	ans.append(temp)
np.savetxt('answer.txt',ans,fmt="%s")
showDataTraining(c1New,c2New,c3New,c4New,c5New,c6New,test,nearTest,"test")
print("File hasil clustering data testing dapat dilihat di: answer.txt")