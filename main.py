import numpy as keshav

# a = keshav.array([1,2,3,4,5])
# print(a)
# print(type(a))
# print(a[1])
# print(a[1:4])
# a[3]=453
# print(a)
a_mul=keshav.array([[[1,2,3,4],[4,5,6,4],[7,8,9,4]],
                   [[1,2,3,4],[4,5,6,4],[7,8,9,4]],
                   [[1,2,3,4],[4,5,6,4],[7,8,9,4]]])
print(a_mul.shape)
print(a_mul.ndim)
print(a_mul.size)
print(a_mul.dtype)