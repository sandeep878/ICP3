import numpy as np
vec=np.arange(1,21,dtype=float)
print(vec)
vec=vec.reshape(4,5)
print(vec)
vec=np.where(np.isin(vec,vec.max(axis=1)),0,vec)
vec