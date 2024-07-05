import numpy as np
from typing import List

class ReshapeMatrix:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        try:
            arr= np.array(mat)
            newarr= arr.reshape(r, c)
            return newarr.tolist()
        
        except BaseException as e:
            return mat      