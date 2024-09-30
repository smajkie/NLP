import numpy as np

a1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a2 = np.array([[1, 2, 3], [3, 4, 5], [7, 8, 9]])    # 3x3 two dimensional array
a3 = np.array([[[1, 2, 3], [3, 4, 5]], [[7, 8, 9], [10, 11, 12]]]) # 2x2x3 three dimensional array
         
print(a1.shape, a2.shape, a3.shape)

a10 = np.arange(1, 10)

if a1.all() == a10.all():       #if a1 == a10: ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
    print("a1 and a10 are equal")

a11 = np.arange(1, 30, 2).reshape(3, 5)
print(a11)

a12 = np.al
