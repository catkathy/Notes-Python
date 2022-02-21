# Define Array
a = np.array([2,23,4], dtype = np.float) #define array type: int, float
print(a.dtype)

# Create Array
a = np.array([[2,23,4],
            [2,32,4]])
print(a)

# Create an array of all 0s
a = np.zeros((3,4)) #zero+s 
print(a)

# Create an array of all 1s and define type
a = np.ones((3,4), dtype = np.int16)
print(a)

# Empty random generate, need to restart the kernel
a = np.empty((3,4))
print(a)

# range 生成数列
a = np.arange(10,20,2)
print(a)

# 生成三行四列从0-11的数列
a = np.arange(12).reshape((3,4))
print(a)

# 生成20段从1-10的线段
a = np.linspace(1,10,20)
print(a)

# 生成6段从1-10的线段，转换成2行3列
a = np.linspace(1,10,6).reshape((2,3))
print(a)
