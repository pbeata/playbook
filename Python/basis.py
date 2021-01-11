import numpy as np

def basis_0(N, u, ui, uj):
  if (ui <= u) and (u < uj):
    N = 1.0
  else:
    N = 0.0


knot_vector = [0, 2, 3, 6]
N = 0.0
n = 10

for i in range(0, len(knot_vector)):
  print("i = %d" % i)

u = np.linspace(knot_vector[0], knot_vector[-1], num=n)
for x in u:
  print("u[i] = %f" % x)

