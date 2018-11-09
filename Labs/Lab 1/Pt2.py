import matplotlib.pyplot as plt
from numpy import *

v = array([1,2,3,4])
print(v)

M = array([[1,2], [3,4]])
print(M)

print(v.shape)
print(M.shape)

print(shape(v))
print(shape(M))

print(M.dtype)

M = array([[1, 2], [3, 4]], dtype=complex)
print(M)

x = arange(0, 2, 0.2)
print(x)

print(linspace(0,10,25))
print(logspace(0,10,10,base=e))
print('Meshgrid:\n', mgrid[0:5, 0:5])

# data = genfromtxt('stockholm_td_adj.dat')
# print(shape(data))

# fig, ax = plt.subplots(figsize=(14,4))

# ax.plot(data[:,0] + data[:,1]/12.0 + data[:,2]/365, data[:,5])
# ax.axis('tight')
# ax.set_title('tempeatures in Stockholm')
# ax.set_xlabel('year')
# ax.set_ylabel('temperature (C)')
#plt.show()

M = random.rand(3,3)
print(M)
savetxt('random-matrix.csv', M)
savetxt('random-matrix_fmt.csv', M, fmt='%.5f')

#For working with numpy native format
save('random-matrix.npy', M)
N = load('random-matrix.npy')
#print(N)

print(M.itemsize, M.nbytes, M.ndim)