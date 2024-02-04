import numpy as keshav

# a = keshav.array([1,2,3,4,5])
# print(a)
# print(type(a))
# print(a[1])
# print(a[1:4])
# a[3]=453
# print(a)
# a_mul=keshav.array([[[1,2,3,4],[4,5,6,4],[7,8,9,4]],
#                    [[1,2,3,4],[4,5,6,4],[7,8,9,4]],
#                    [[1,2,3,4],[4,5,6,4],[7,8,9,4]]])
# print(a_mul.shape)
# print(a_mul.ndim)
# print(a_mul.size)
# print(a_mul.dtype)
# a=keshav.array([[1,2,3],
#                [4,5,"keshavraj"],
#                [7,"pore",8]])#,dtype=keshav.int32 can used when we have string of int data type it will convert it into int32

# print(a.dtype)
# print(type(a[0][0]))
# print(a[0][0].dtype)
# print(a[1][2])#it will print the element from list 1 element 2
# print(a.ndim)

# dictionary
# d={'1':'a'}

# a=keshav.array([[1,2,3],
#                [4,d,"keshavraj"],
#                [7,"pore",8]])#if we want to create any array to string we just have to use ,dtype="<u2"
# print(a.dtype)
# print(type(a[1][1]))

#
# k=keshav.full((1,2,3),9)#fill with one element
# print(k)
# k=keshav.zeros((4,5,3))
# print(k)
# k=keshav.empty((5,5,5))
# print(k)
# # printing values
# values=keshav.arange(0,453,3)
# print(values)
# values=keshav.linspace(0,453,454)
# print(values)
# print(keshav.nan)
# print(keshav.inf)
# print(keshav.isnan(keshav.sqrt(-1)))
# print(keshav.isinf(keshav.array([10])/0))
# print(keshav.sqrt(-1))
# print(keshav.array([10])/0)
#mathematical operation
# l1=[1,2,3,4]
# l2=[4,5,6,7]
# a1=keshav.array(l1)
# a2=keshav.array(l2)
# print(l1*5)#its not like vector only multiply works
# print(a1*5)#it multiply each element by5   its like vector it can add multiply divide so on
 
# a1=keshav.array([1,3,4])
# a2=keshav.array([[2],[4]])
# print(a1 + a2)
# print(keshav.sin(a1))#we can use cos tan log square root and so on


#append delete modify so on on array
a=keshav.array([[1,2,3],[4,5,5]])
print(keshav.delete(a,4))
print(keshav.delete(a,5))
print(keshav.delete(a,0,0))
print(keshav.delete(a,1,1))
#reshaping 
print(a.shape)
print(a.reshape(3,2))
print (a.transpose)
print(a.swapaxes(0,1))
#for mergin two array 
p=keshav.array([[1,2,3],[4,5,5]])
o=keshav.array([[1,2,3],[4,5,5]])
l=keshav.concatenate((p,o), axis=1)
print(l)
j=keshav.stack((p,o))# also have vstack and hstack v for vertical and h for horizontal
print(j)
# split is used for spliting the array in many part for this 
# use print(keshav.split(a,5,axis=1))
print(a.min())
print(a.max())
print(a.mean())
print(a.std())
print(keshav.median(a))

#random values 
number=keshav.random.randint(90,100,size=(2,3,4))
print(number)
# keshav.savetxt("keshavraj1.csv",p,delimiter=",")
v=keshav.load("keshavraj.npy")
print(v)
z=keshav.loadtxt("keshavraj1.csv",delimiter=",")
print(z)