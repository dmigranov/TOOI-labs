import numpy as np
#axis 0 - rows, axis 1 - cols
#1
z = np.zeros(10)
print(z)
#2
z[9] = 1
print(z)
#3
print(np.full(10, 14.8))
#4
a = np.arange(23, 39, 1)
print(a)
#5
#print(flipud(a))
print(a[::-1]) # x:y:z x - start index, z -step size, y = end index
#6, 7
print(np.reshape(np.arange(0, 9, 1), (3,3)))
#8
print(np.nonzero([1,2,0,0,4,0]))
#9
r = np.random.random((10,10))
print(np.amax(r), np.amin(r))
#10
r = np.random.random(15)
print(np.argmax(r), np.argmin(r))
#11
r = np.random.random(30)
print(np.mean(r))
#12
r = np.random.random((3,10))
print(np.mean(r, 0))
print(np.mean(r, 1))
#13
r = np.random.random((3,3))
print(np.pad(r, 1, 'constant', constant_values=0))
#14
print(np.dot(np.random.random((5,3)), np.random.random((3,2))))
#15
r1 = np.random.randint(1,10, 10) #[low, high)
r2 = np.random.randint(1,10, 10)
print(np.intersect1d(r1, r2))
#16
print(np.sort(np.random.random(10)))
#17
r = np.random.random(10)
r[np.argmax(r)] = 0
print(r)
#18
r = np.random.random((3,3))
print(np.reshape(r, 9))
#19
r = np.random.random((4,4))

#20
with open('matrix.txt', 'r') as source:
    print(np.fromfile(source, sep=','))

