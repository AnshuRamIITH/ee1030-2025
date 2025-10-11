import ctypes
import numpy as np

lib = ctypes.CDLL("./func.so")
lib.matmul.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"), 
    np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"), 
]
lib.matmul.restype = None
A = np.array([[2, 4],
              [-1, 2]], dtype=np.float64)
B = np.array([[1/3, -2/3],
              [1/6, 1/3]], dtype=np.float64)

C = np.zeros((2, 2), dtype=np.float64)
lib.matmul(A, B, C)

print("C = A*B =\n", C)
