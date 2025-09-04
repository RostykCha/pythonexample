import numpy as np

values1 = np.array([1, 2, 3], dtype=np.int32)
values2 = np.arange(1, 1000, 2)

print(type(values2))

print(values2 / 2)
print(np.max(values2))
print(np.min(values2))
print(np.mean(values2))
print(np.sum(values2))