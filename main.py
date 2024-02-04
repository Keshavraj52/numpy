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
a=keshav.array([[1,2,3],
               [4,5,"keshavraj"],
               [7,"pore",8]])#,dtype=keshav.int32 can used when we have string of int data type it will convert it into int32

print(a.dtype)
print(type(a[0][0]))
print(a[0][0].dtype)
print(a[1][2])#it will print the element from list 1 element 2
print(a.ndim)