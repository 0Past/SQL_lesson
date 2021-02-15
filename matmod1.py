import numpy as np
k = int(input())
p =np.array([[0.1, 0.4, 0.5],
             [0.3, 0.2, 0.5],
             [0.6, 0.35, 0.05]])

A = np.array([0.1, 0.2, 0.3])

task1 = np.linalg.matrix_power(p, k)

task2 = np.dot(A, task1)

print(p)
print("\nTask1\n", task1)
print("\nTask2\n", task2)




